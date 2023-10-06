import json
import requests

r = requests.get('https://www.amiiboapi.com/api/amiibo/?amiiboSeries=Super%20Mario%20Bros.')
#print(r.text)
data = r.json()
#print para ver el nombre de los todos los amiibos
for i in data['amiibo']:
   print(i['name'])