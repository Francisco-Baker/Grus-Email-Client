import requests
import time

ip = requests.get('http://myip.ipip.net', timeout=5).text
print(ip)
time.sleep(5.0)