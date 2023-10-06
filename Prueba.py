import json
import requests

r = requests.get('https://www.amiiboapi.com/api/amiibo/?amiiboSeries=Super%20Mario%20Bros.')
print(r.text)
