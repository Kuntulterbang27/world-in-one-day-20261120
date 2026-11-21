"""Offline acceptance tests for the exact sandbox entry."""
from pathlib import Path
import hashlib
import os
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

ROOT = Path(__file__).resolve().parent


class EntryContract(unittest.TestCase):
    def test_entry_writes_one_complete_deterministic_image(self):
        self.assertTrue((ROOT / "main.py").is_file(), "Missing sandbox entrypoint")
        runs = []
        for seed in ("1", "923"):
            with tempfile.TemporaryDirectory() as directory:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=directory, PYTHONHASHSEED=seed)
                subprocess.run([sys.executable, "-B", "-P", "-s", str(ROOT / "main.py")],
                               env=env, check=True, timeout=10, cwd=directory)
                files = list(Path(directory).iterdir())
                self.assertEqual([p.name for p in files], ["entry.png"])
                data = files[0].read_bytes()
                self.assertLessEqual(len(data), 1048576)
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                offset = 8
                types = []
                while offset < len(data):
                    length = struct.unpack(">I", data[offset:offset + 4])[0]
                    tag = data[offset + 4:offset + 8]
                    payload = data[offset + 8:offset + 8 + length]
                    crc = struct.unpack(">I", data[offset + 8 + length:offset + 12 + length])[0]
                    self.assertEqual(zlib.crc32(tag + payload) & 0xffffffff, crc)
                    if tag == b"IHDR":
                        self.assertEqual(struct.unpack(">II", payload[:8]), (1024, 1024))
                    types.append(tag)
                    offset += length + 12
                self.assertEqual(offset, len(data))
                self.assertEqual(types[-1], b"IEND")
                runs.append(data)
        self.assertEqual(runs[0], runs[1], "Output differs between fresh runs")
        self.assertEqual(runs[0], (ROOT / "news.png").read_bytes())
        print("VERIFIED PNG SHA256", hashlib.sha256(runs[0]).hexdigest(), "BYTES", len(runs[0]))


if __name__ == "__main__":
    unittest.main()
