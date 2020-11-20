import time
import requests
url = os.environ["URLS"]
url = url.split(" ")
while True:
  for i in url:
    status = requests.get(i).status_code
    print(f"response of {i} = {status}")
  time.sleep(60)
