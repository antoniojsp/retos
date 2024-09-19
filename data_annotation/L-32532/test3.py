import schedule
import time
import requests

def call_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", headers={"Authorization": "Bearer dummy_api_key"})
    print(response.json())

schedule.every(3).seconds.do(call_api)

while True:
    schedule.run_pending()
    time.sleep(1)