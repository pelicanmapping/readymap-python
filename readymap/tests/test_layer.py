import unittest

from readymap import ReadyMap

class TestLayer(unittest.TestCase):
    def setUp(self):
        # Login
        self.rm = ReadyMap("http://localhost:8000", username="readymap", password="readymap")

    def create_layer(self, name):
        return self.rm.create_layer({
        "apply_742_colorization": False,
        "apply_background_color": False,
        "background_color": "",
        "data_type": 1,
        "description": "",
        "enabled": True,
        "format": "png",
        "generate_tiles_on_demand": True,
        "make_similar_background_colors_transparent": False,
        "max_level": 19,
        "metatile": False,
        "name": "My Layer",
        "public": True,
        "resample": 0,
        "spherical_mercator": False,
        "tile_size": 256,
        "time": "2014-08-21T17:09:00Z",
        "layer_type": "local"
        })

    def test_create_delete(self):
        # Create a layer
        layer = self.create_layer("My new layer")
        self.assertTrue(hasattr(layer, "id"))

        # List all the layers and make sure our new layer is in there
        layers = self.rm.get_layers()

        found = False
        for l in layers:
            if l.id == layer.id:
                found = True
                break
        self.assertTrue(found)

        # Now modify the layer
        layer.name = "Taco"
        layer.save()

        # Get the layer from the server and make sure the name has changed.
        newLayer = self.rm.get_layer(id=layer.id)
        self.assertEqual(layer.name, newLayer.name)

        # Now delete the layer
        layer.delete()


if __name__ == '__main__':
    unittest.main()