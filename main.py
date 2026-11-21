"""Python 3.13 sandbox entry: standard library only; no network or Pillow."""
from pathlib import Path
import os
import shutil


def main():
    source = Path(__file__).resolve().with_name("news.png")
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True, mode=0o755)
    target = output / "entry.png"
    shutil.copyfile(source, target)
    target.chmod(0o644)


if __name__ == "__main__":
    main()
