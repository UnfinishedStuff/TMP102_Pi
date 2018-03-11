import time
import TMP102

try:
	while True:
		print("{:.2f}".format(TMP102.get_temp()) + "*C")
		time.sleep(0.5)
except KeyboardInterrupt:
	print("Manually stopped.")
