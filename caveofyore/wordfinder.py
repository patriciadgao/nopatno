import requests 

r = requests.get(url = "https://random-word-api.herokuapp.com/all") 


data = r.json()

print(','.join(data))