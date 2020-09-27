import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'var15':72, 'var167':2.3, 'var5':88, 'var228':-25.0, 'var93':0})


print(r.json())