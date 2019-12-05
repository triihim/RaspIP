import os
from time import sleep
from utils import is_connected, get_ip, get_ssid
from config import CONN_CHECK_INTERVAL
import logger
import sender

sleep(20) # Prevents script from starting immediately
logger.log("Watcher started")

interval = CONN_CHECK_INTERVAL
connected = is_connected()

last_known_ssid = ""

if interval < 30:
	interval = 30

if connected:
	# SEND EMAIL ON BOOT
	ip = str(get_ip())
	ssid = str(get_ssid())
	last_known_ssid = ssid
	sender.send_mail("RaspIP", ssid + ": " + ip)
	logger.log("Email sent on boot with following data: " + ssid + ", " + ip)

while True:
	connected = is_connected()
	print("Connected: " + str(connected))
	if not connected:
		logger.log("Watcher triggering reconnect")
		os.system("python3 reconnect.py &")
	elif str(get_ssid()) != last_known_ssid:
		# Network has changed
		logger.log("Network has changed from " + last_known_ssid + " > " + str(get_ssid()))
		sender.send_mail("RaspIP", str(get_ssid()) + ": " + str(get_ip()))
		last_known_ssid = str(get_ssid())
	sleep(interval)
