import requests, json
import time

'''
result =  requests.get("http://www.threatcrowd.org/searchApi/v2/email/report/", params = {"email": "EMAIL_ADRESS"})
print result.text
j = json.loads(result.text)
print j['domains'][0]
'''

print requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": "aoldaily.com"}).text

print requests.get("http://www.threatcrowd.org/searchApi/v2/ip/report/", {"ip": "188.40.75.132"}).text

print requests.get("http://www.threatcrowd.org/searchApi/v2/antivirus/report/", {"antivirus" :"plugx"}).text



