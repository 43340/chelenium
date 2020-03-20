import json
import os

def test_data_provider(page):
    try:
        path = os.path.dirname(os.path.realpath(__file__)) + f"/data_{page}.json"
        with open(path, 'r') as data_provider:
            data = json.load(data_provider)
        return data

    except:
        raise Exception("No JSON found.")