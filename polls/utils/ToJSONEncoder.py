from json.encoder import JSONEncoder


class ToJSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
