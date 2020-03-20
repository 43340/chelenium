import json
import os

def test_data_provider(page, data_name):
    try:
        path = os.path.dirname(os.path.realpath(__file__)) + f"/data_{page}.json"
        with open(path, 'r') as data_provider:
            data = json.load(data_provider)
        return data.get(data_name)

    except:
        raise Exception("No JSON found.")