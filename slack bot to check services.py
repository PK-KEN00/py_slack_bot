import subprocess
import os
import subprocess
import requests

# to post message in slack
class Slack:
    def __init__(self,report):
        webhook = 'https://hooks.slack.com/services/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'
        response = requests.post(webhook, json=report, headers={'Content-Type': 'application/json'})
        if response.ok:
            json_data = response.text
            self.result = json_data
def is_service_running(name):#function for service is running or stopped
        with open(os.devnull, 'wb') as hide_output:
            exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
            return exit_code == 0
def service_status(services_list):
    for name in services_list:
        if not is_service_running(name):
            print("services not Running")
            active=subprocess.getoutput
            result_dict = ("*"+name+"  Service is not running* ")
            slack_report = {"attachments": [{"fallback": "*ASUS X507UF*", "color": "#FF0000", "text": result_dict}]}
            slack_push_log = Slack(slack_report)
        else:
            print("Is running")
            result_dict = ("*"+name+" Service is  running* ")
            slack_report = {"attachments": [{"fallback": "*ASUS X507UF*", "color": "#3CB043", "text": result_dict}]}
            slack_push_log = Slack(slack_report)
# to get all services running or stopped in  server            
cmd = "systemctl list-units --all"
output = subprocess.getoutput(cmd)

cmd_list = list(output.split(" ")) 
services_array =[]
for i in range (0,len(cmd_list)):
    if(cmd_list[i].endswith(".service")):
        services_array.append(cmd_list[i].replace(".service",""))
# print(services_array)

services=services_array

service_status(services)