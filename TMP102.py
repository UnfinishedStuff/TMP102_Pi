from smbus2 import SMBusWrapper,i2c_msg
import time

address = 0x48

def getTemperature():
	with SMBusWrapper(1) as bus:
		temperature_write = i2c_msg.write(address, [0x00])
		temperature_read = i2c_msg.read(address,2)
		bus.i2c_rdwr(temperature_write)
		time.sleep(0.1)
		bus.i2c_rdwr(temperature_read)	

	data = list(temperature_read)
	#print(str(data[0]) + " " + str(data[1]))
	data[0] = data[0] * 256

	temperature = data[0] + data[1]
	temperature = (temperature >> 4)  * 0.0625

	return(temperature)
	
while True:
	temp = getTemperature()
	print(round(temp,2))
	time.sleep(0.5)
