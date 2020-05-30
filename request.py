import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'date':25/0/2020, 'time':18:00:00})

print(r.json())
