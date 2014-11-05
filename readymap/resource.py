import json
import requests

class ReadymapObject(object):
    """
    Base object
    """
    def __init__(self, id=None):
        super(ReadymapObject, self).__init__()
        if id:
            self.id = id
        self._client = None

    @classmethod
    def new(cls, client, type, data):
        payload = json.dumps(data)
        headers = client.headers
        headers['Content-type'] = 'application/json'
        headers['Accept'] = 'text/plain'
        resp = requests.post(client.abs_path(type.class_url()) + "/", data=payload, headers=headers)
        # Create a new object of the given type
        new = type()
        new._client = client
        new.decode(resp.json())
        return new

    @classmethod
    def all(cls, client, type):
        r = requests.get(client.abs_path(type.class_url()), headers=client.headers)
        j = r.json()
        results = []
        for item in j:
            obj = type()
            obj._client = client
            obj.decode(item)
            results.append(obj)
        return results

    def fetch(self, client):
        r = requests.get(client.abs_path(self.instance_url), headers=client.headers)
        j = r.json()
        self.decode(j)
        self._client = client

    def save(self):
        payload = json.dumps(self.encode())
        headers = self._client.headers
        headers['Content-type'] = 'application/json'
        headers['Accept'] = 'text/plain'
        requests.put(self._client.abs_path(self.instance_url), data=payload, headers=headers)

    def delete(self):
        """
        Deletes a resource
        """
        requests.delete(self._client.abs_path(self.instance_url), self._client.headers)

    def encode(self):
        data = {}
        for k, v in self.__dict__.iteritems():
            if not k.startswith("_"):
                data[k] = v
        return data

    def decode(self, data):
        for k, v in data.iteritems():
           setattr(self,k,v)


class Layer(ReadymapObject):
    def __init__(self, *args, **kwargs):
        super(Layer, self).__init__(*args, **kwargs)

    @classmethod
    def class_url(cls):
        """
        Gets the base url for this resource
        """
        return "/api/layers"

    @property
    def instance_url(self):
        """
        Gets the url for this Layer
        """
        base = self.class_url()
        return "%s/%s" % (base, self.id)

    def get_files(self):
        """
        Gets the files for this layer if it's a Local layer
        """
        if self.TypeString == "Local":
            url = self._client.abs_path(self.instance_url + "/files")
            r = requests.get(url, self._client.headers)
            return r.json()
        return None

    def publish(self):
        """
        Publishes this layer
        """
        url = self._client.abs_path("/layers/%s/publish" % self.id)
        requests.post(url, self._client.headers)

    def __str__(self):
        return "Layer: %s" % self.name

