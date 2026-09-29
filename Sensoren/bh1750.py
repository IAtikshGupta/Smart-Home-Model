import smbus2
import time

sensor = smbus2.SMBus(1)
address = 0x23

def read_bh1750():
    sensor.write_byte(address, 0x20)
    time.sleep(0.12)
    val = sensor.read_i2c_block_data(address, 0x00, 2)
    lux = (val[0] << 8 | val[1]) / 1.2
    return lux