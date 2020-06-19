import json
import sys
import urllib3
from csv import DictReader
from functions import *

ip = input("IP? ")
sid = login(ip)
port = "443"
#loading in file
with open('host.csv', 'r') as read_obj:
    object
    #reading file
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        #setting variables to send to api
        new_host_data = {'name':row['hostname'], 'ip-address':row['host_ip']}
        new_host_result = api_call(ip, port, 'add-host', new_host_data, sid)
        print(json.dumps(new_host_result))
        
#publishes the hosts        
api_call(ip, port, 'publish', {}, sid)

#logouts out of the session
logout_result = api_call(ip, port, 'logout', {}, sid)
print("logout result: " + json.dumps(logout_result))	