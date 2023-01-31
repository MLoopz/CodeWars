import json
def jsonattr(filepath):
    with open(filepath) as f:
        jsn = json.load(f)
    print(jsn)
    obj = JsonClass(jsn)
    return obj
    
class JsonClass(object):
    def __init__(self, jsn):
        for key in jsn:
            setattr(self, key, jsn[key])
        

print(jsonattr("json.json"))