from time import sleep
from utils import get_ssid, get_ip, is_connected
import os
import logger
import sender

def reconnect():
	connectCmd = "wpa_cli -i wlan0 reconfigure &"
	logger.log("Reconnecting...")
	os.system(connectCmd)

if is_connected():
	ip = str(get_ip())
	ssid = str(get_ssid())
	sender.send_mail("RaspIP", ssid + ": " + ip)
else:
	reconnect()

