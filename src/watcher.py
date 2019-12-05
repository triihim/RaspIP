import os
from time import sleep
from utils import is_connected

while True:
	connected = is_connected()
	print("Connected: " + str(connected))
	if not connected:
		print("Watcher triggering reconnect")
		os.system("python connect.py")
	sleep(30)
