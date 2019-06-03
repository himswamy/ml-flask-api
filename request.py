import requests, json



url = 'http://0.0.0.0:5000/api/'



data = [[24.00, 68.10, 17.21, 10.00, 9.0, 12.8, 10.31, 1.53, 2.5, 0.411, 4.7, 8.2, 0.572, 0.571, 2, 3.2, 0.611, 3.5, 4.2, 7.7, 0.6, 0.5, 0.1, 0.5, 1.7, 6.00]]


j_data = json.dumps(data)


headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers)

print(r,r.text)


