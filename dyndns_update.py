import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

BASE_URL = "https://dyndns.inwx.com/nic/update"
HOSTS = os.getenv("DYNDNS_HOSTS")
PASSWORD = os.getenv("DYNDNS_PASSWORD")

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


for host in HOSTS.split(","):
    basic = HTTPBasicAuth(host, PASSWORD)
    url = f"{BASE_URL}?hostname={host}"
    if ipv4:
        url += f"&myip={ipv4}"
    if ipv6:
        url += f"&myipv6={ipv6}"

    r = requests.post(url, auth=basic)
