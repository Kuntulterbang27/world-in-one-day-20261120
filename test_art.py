"""A visual-content regression test, independent of layout implementation."""
from pathlib import Path
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parent


class GeographyRegression(unittest.TestCase):
    def test_world_map_has_visible_land(self):
        with Image.open(ROOT / "news.png") as image:
            colors = image.crop((657, 137, 983, 276)).convert("RGB").get_flattened_data()
            land_pixels = sum(color == (108, 133, 136) for color in colors)
        self.assertGreater(land_pixels, 2500,
                           "Map needs recognizable land, not only a grid and dots")


if __name__ == "__main__":
    unittest.main()
