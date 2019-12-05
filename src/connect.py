from time import sleep

def reconnect():
	connectCmd = "wpa_cli -i wlan0 reconfigure"
	os.system(connectCmd)

MAX_TRIES = 10
tries = 0

while tries < MAX_TRIES:
	if is_connected():
		print("We have connection!")
		print(get_ssid())
		print(get_ip())
		break
	else:
		tries += 1
		print("Reconfiguring attempt " + str(tries))
		reconnect()
	sleep(20)
