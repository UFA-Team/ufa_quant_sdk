import requests
from config import API_KEY

def _post_request(site, endpoint, payload):
    payload['API_KEY'] = API_KEY
    r = requests.post(site + endpoint, json=payload, timeout=5)
    return r

def _get_request(site, endpoint, payload):
    payload['API_KEY'] = API_KEY
    r = requests.get(site + endpoint, params=payload, timeout=5)
    return r



