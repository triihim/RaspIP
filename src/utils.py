import os
import socket
import re

def is_connected():
	try:
		socket.create_connection(("www.google.com", 80))
		return True
	except:
		pass
	return False

def get_ip():
	ifconfig = os.popen("ifconfig wlan0").read()
	ip_pattern = "inet (?P<ip>[^\s]+)"
	match = re.search(ip_pattern, ifconfig)
	return match.group("ip")

def get_ssid():
	iwgetid = os.popen("iwgetid").read()
	ssid_pattern = 'ESSID:"(?P<ssid>[^$"]+)'
	match = re.search(ssid_pattern, iwgetid)
	return match.group("ssid")
