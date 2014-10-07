import json

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
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = client._session.post(client.abs_path(type.class_url()) + "/", data=payload, headers=headers)
        # Create a new object of the given type
        new = type()
        new.decode(resp.json())
        return new

    def fetch(self, client):
        r = client._session.get(client.abs_path(self.instance_url))
        j = r.json()
        self.decode(j)
        self._client = client

    def save(self):
        payload = json.dumps(self.encode())
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self._client._session.put(self._client.abs_path(self.instance_url), data=payload, headers=headers)

    def delete(self):
        """
        Deletes a resource
        """
        self._client._session.delete(self._client.abs_path(self.instance_url))

    def __str__(self):
        return str(self.dict)

class Layer(ReadymapObject):
    def __init__(self, *args, **kwargs):
        super(Layer, self).__init__(*args, **kwargs)

    @classmethod
    def class_url(cls):
        return "/api/layers"

    @property
    def instance_url(self):
        base = self.class_url()
        return "%s/%s" % (base, self.id)

    def encode(self):
        data = {}
        for k, v in self.__dict__.iteritems():
            if not k.startswith("_"):
                data[k] = v
        return data

    def decode(self, data):
        for k, v in data.iteritems():
           setattr(self,k,v)
        self.encode()