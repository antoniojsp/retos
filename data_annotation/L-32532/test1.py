import requests

url = "http://127.0.0.1:5000/"
headers = {"Authorization": "7281fae460d84fde91d83514240709"}
data = {"param1": "value1ddd", "param2": "value2"}


response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    data = response.json()
    print(data)
    # Process the data
else:
    print("Error:", response.text)