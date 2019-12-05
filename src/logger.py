from datetime import datetime

def log(msg):
	with open("../logs", "a") as f:
		ts = datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
		f.write(ts + "\t" + msg + "\n")

