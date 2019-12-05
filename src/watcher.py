import os
from time import sleep
from utils import is_connected, get_ip, get_ssid
from config import CONN_CHECK_INTERVAL
import sender

interval = CONN_CHECK_INTERVAL
connected = is_connected()

if interval < 30:
	interval = 30

if connected:
	# SEND EMAIL ON BOOT
	ip = str(get_ip())
	ssid = str(get_ssid())
	sender.send_mail("RaspIP", ssid + ": " + ip)

while True:
	connected = is_connected()
	print("Connected: " + str(connected))
	if not connected:
		print("Watcher triggering reconnect")
		os.system("python3 reconnect.py")
	sleep(interval)
