import requests

sample = {
    "squareMeters": 75523,
    "numberOfRooms": 3,
    "hasYard": 0,
    "hasPool": 1,
    "floors": 63,
    "cityCode": 9373,
    "cityPartRange": 3,
    "numPrevOwners": 8,
    "made": 2005,
    "isNewBuilt": 0,
    "hasStormProtector": 1,
    "basement": 4313,
    "attic": 9005,
    "garage": 956,
    "hasStorageRoom": 0,
    "hasGuestRoom": 1
}

url = "http://localhost:9696/predict"
response = requests.post(url, json=sample)
print(response.json())