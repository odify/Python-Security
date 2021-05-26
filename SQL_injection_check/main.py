#!/usr/bin/env python3


import requests
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint


s = requests.Session()

# z.B Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.39

s.headers["User-Agent"] = ""
login_payload = {

     "username": "admin123",
     "password": "password123",

     "Login": "Welcome, $username ! ",
}


login_url = "http://localhost:8080/DVWA-master/login.php"

r = s.get(login_url)

token = re.search("user_token'\s*value='(.*?)'", r.text).group(1)

login_payload['user_token'] = token

s.post(login_url, data=login_payload)


def get_all_forms(url):
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def is_vulnerable(response):
    errors = {
        "error in sql syntax;",
        "warning: mysql",
        "no quotationmarks",
        "another syntax error",
    }
    for error in errors:
        if error in response.content.decode().lower():

            return True

    return False


def scan_sql_injection(url):
    for c in "\"'":
        new_url = f"{url}{c}"

        print("[!] Trying", new_url)


        res = s.get(new_url)
        if is_vulnerable(res):
            print("[+] SQL Injection vulnerability detected, link:", new_url)
            return

    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":

            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["value"] or input_tag["type"] == "hidden":
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:

                        pass

                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{c}"

            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":

                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)


            if is_vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link:", url)
                print("[+] Form:")
                pprint(form_details)
                break   



if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    scan_sql_injection(url)


