import time
import requests
import os

url = os.environ["URLS"]
url = url.split(" ")
while True:
  for i in url:
    status = requests.get(i).status_code
    print(f"response of {i} = {status}")
  time.sleep(int(os.environ["INTERVAL"]))
