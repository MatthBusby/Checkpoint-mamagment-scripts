import requests
import json
import sys
import getpass


#does api calls to smartconsole
def api_call(ip_addr, port, command, json_payload, sid):
    url = 'https://' + ip_addr + ':' + port + '/web_api/' + command
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
    return r.json()



#login API call that returns SID
def login(ip):
    payload={}
    payload['user'] = input("username? ")
    payload['password'] = getpass.getpass('Password?')

    headers = {
        'content-type': "application/json",
        'Accept': "*/*" 
    }

    response = requests.post("https://"+ip+"/web_api/login", json=payload, headers=headers, verify=False)
    response.raise_for_status()
    jsonResponse = response.json()
    sid = jsonResponse['sid']
    return sid