import json
import requests
import urllib.parse

BASE_URL = r"https://api.redtube.com/?"


GENERATE_URL = "{}={}"

def output(output_type, data):
    if output_type.lower() == "json":
        return json.loads(data)
    return data
