import requests

try:
    requests.get("https://hc-ping.com/your-uuid-here", timeout=10)
except requests.RequestException as e:
    # Log ping failure here...
    print("Ping failed: %s" % e)v



import socket
import urllib.request

try:
    urllib.request.urlopen("https://hc-ping.com/your-uuid-here", timeout=10)
except socket.error as e:
    # Log ping failure here...
    print("Ping failed: %s" % e)


# Passing diagnostic information in the POST body:
import requests
requests.post("https://hc-ping.com/your-uuid-here", data="temperature=-7")


