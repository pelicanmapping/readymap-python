ReadyMap Python bindings
=========================

This is a Python interface for interacting with the API of Pelican Mapping's ReadyMap server.

For more information about ReadyMap:  http://www.readymap.org

# Installation

To install the latest from Github you can run

     sudo pip install git+https://github.com/pelicanmapping/readymap-python.git
     
# Getting Started

Here are just some of the amazing things you can do with the ReadyMap API

```python

from readymap import ReadyMap

# Login to the server
rm = ReadyMap("http://yourserver.com/readymap", username="username", password="password")

# List all the layers on the server
layers = rm.get_layers()
for l in layers:
   print l.name
   
# Get a specific layer
l = rm.get_layer(id=10)

# Edit a layer
l.name = "My new name"
l.save()

# Publish a layer
l.publish()

# Delete a layer
l.delete()

# Create a brand new layer
new_layer = rm.create_layer({
   "data_type": 1,
   "description": "",
   "format": "png",
   "generate_tiles_on_demand": True,
   "max_level": 19,
   "name": "My Layer",
   "public": True,
   "resample": 0,
   "spherical_mercator": False,
   "tile_size": 256,
   "time": "2014-08-21T17:09:00Z",
   "layer_type": "local"
   })
   
# Upload a file to the server
rm.upload(directory="/myuploads", filename="/path/to/image.tif")

# Upload a file to the server and create a layer
rm.upload_layer(name="My Uploaded Layer", description="A new layer", files=["/path/to/image.tif",])
```
      

    
    
    
