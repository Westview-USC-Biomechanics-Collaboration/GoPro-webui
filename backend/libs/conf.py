import json
import os

def get_conf():
    with open(os.path.join(os.path.dirname(__file__), os.pardir, 'conf.json')) as data:
        conf = json.load(data)
    return conf