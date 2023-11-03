import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

USER = os.getenv("DYNDNS_USER")
PASSWORD = os.getenv("DYNDNS_PASSWORD")
BASE_URL = "https://dyndns.inwx.com/nic/update"
MY_URL = "cloud.palebluedot.dev"

basic = HTTPBasicAuth(USER, PASSWORD)

ipv4 = None
try:
    ipv4 = requests.get("https://api.ipify.org").text
except Exception:
    pass

ipv6 = None
try:
    ipv6 = requests.get("https://api64.ipify.org").text
except Exception:
    pass

url = f"{BASE_URL}?hostname={MY_URL}"
if ipv4:
    url += f"&myip={ipv4}"
if ipv6:
    url += f"&myipv6={ipv6}"

r = requests.post(url, auth=basic)
