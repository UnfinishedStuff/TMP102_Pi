from smbus import SMBus
bus = SMBus(1)

address = 0x48

def get_temp():

	data = bus.read_i2c_block_data(0x48, 0x00, 2)

	data[0] = data[0] * 256

	temperature = data[0] + data[1]
	temperature = (temperature >> 4)  * 0.0625

	return(temperature)
