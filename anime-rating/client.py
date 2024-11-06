'''
Script for inferencing the deployed model
'''

import json
import requests

data = [[64, 8.0, 1, 0, 1, 103707.0, 14351, 25810, 2656, 86547, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 2],
       [16, 8.0, 1, 0, 1, 103707.0, 14351, 25810, 2656, 86547, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 2],
       [1,8.0,0,0,0,22.0,1,29,1,10,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,17]]

url = 'http://0.0.0.0:8001/predict/'

predictions = []
for record in data:
    payload = {'features': record}
    payload = json.dumps(payload)
    response = requests.post(url, data=payload)
    predictions.append(response.json()['predicted_rating'])

print(predictions)
print("Actual Predictions Respectively 4.702, 4.663, 2.87")



