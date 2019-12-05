from time import sleep
from utils import get_ssid, get_ip, is_connected
import os
import sender

def reconnect():
	connectCmd = "wpa_cli -i wlan0 reconfigure"
	os.system(connectCmd)

if is_connected():
	print("We have connection!")
	ip = str(get_ip())
	ssid = str(get_ssid())
	sender.send_mail("RaspIP", ssid + ": " + ip)
else:
	reconnect()

