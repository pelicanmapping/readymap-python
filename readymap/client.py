import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from resource import ReadymapObject, Layer
from readymap import error

class ReadyMap(object):
    """
    Client object for interacting with a ReadyMap server.
    """
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def abs_path(self, path):
        return "%s%s" % (self.url, path)

    @property
    def headers(self):
        return {"Authorization": "token %s" % self.token}

    def get_layers(self):
        """
        Gets all layers from the server
        """
        return ReadymapObject.all(self, Layer)

    def get_layer(self, id):
        """
        Gets a layer from the server
        """
        l = Layer(id=id)
        l.fetch(self)
        return l

    def delete_layer(self, id):
        """
        Deletes a layer
        """
        l = Layer(id=id)
        l.delete(self)

    def create_layer(self, data):
        """
        Creates a layer
        """
        return ReadymapObject.new(self, Layer, data)

    def _create_callback(self, encoder):

        total = len(encoder)

        def callback(monitor):
            percent_complete = 100.0 * float(monitor.bytes_read) / float(total)
            print "Sent %s of %s bytes.  %.2f%% complete" % (monitor.bytes_read, total, percent_complete)

        return callback

    def upload(self, directory, filename):
        """
        Uploads a file to ReadyMap
        """
        # We use the MultipartEncoder to handle streaming large files as well as progress
        encoder = MultipartEncoder({
            "dir": directory,
            "file": (filename, open(filename, 'rb'))
            })
        callback = self._create_callback(encoder)
        monitor = MultipartEncoderMonitor(encoder, callback)
        headers = self.headers
        headers["Content-Type"] = monitor.content_type
        requests.post(self.abs_path("/filemanager/upload_data/"), data=monitor, headers=headers)

    def upload_layer(self, name, description, files):
        """
        Uploads files and creates a new layer
        """
        # We use the MultipartEncoder to handle streaming large files as well as progress
        data = {}
        index = 0
        for f in files:
            data["file%s" % index] = (f, open(f, 'rb'))
            index+=1
        data["name"] = name
        data["description"] = description

        encoder = MultipartEncoder(data)
        callback = self._create_callback(encoder)
        monitor = MultipartEncoderMonitor(encoder, callback)
        headers = self.headers
        headers["Content-Type"] = monitor.content_type
        requests.post(self.abs_path("/layers/upload"), data=monitor, headers=headers)








