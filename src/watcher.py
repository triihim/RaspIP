import os
import socket
import time

def is_connected():
	try:
		socket.create_connection(("www.google.com", 80))
		return True
	except:
		pass
	return False

while True:
	connected = is_connected()
	print("Connected: " + str(connected))
	if not connected:
		print("Watcher triggering reconnect")
		os.system("python connect.py")
	time.sleep(30)
