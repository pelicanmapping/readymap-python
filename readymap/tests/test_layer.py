import unittest

from readymap import ReadyMap

class TestLayer(unittest.TestCase):
    def setUp(self):
        # Login
        self.rm = ReadyMap("http://localhost:8000", username="readymap", password="readymap")

    def test_create(self):
        layer = self.rm.create_layer({
        "apply_742_colorization": False,
        "apply_background_color": False,
        "background_color": "",
        "data_type": 1,
        "description": "dd",
        "enabled": True,
        "format": "png",
        "generate_tiles_on_demand": True,
        "make_similar_background_colors_transparent": False,
        "max_level": 19,
        "metatile": False,
        "name": "My Layer 2",
        "public": True,
        "resample": 0,
        "spherical_mercator": False,
        "tile_size": 256,
        "time": "2014-08-21T17:09:00Z",
        "layer_type": "local"
        })

        print layer.id


if __name__ == '__main__':
    unittest.main()