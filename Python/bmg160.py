# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# BMG160
# This code is designed to work with the BMG160_I2CS I2C Mini Module available from ncd.io
# https://store.ncd.io/product/bmg160-16-bit-triaxial-%C2%B1125s-to-%C2%B12000s-gyroscope-sensor-i2c-mini-module/

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

BMG160_DEFAULT_ADDRESS = 0x68
BMG160_RATE_X_LSB = 0x02

BMG160_RANGE_REGISTER = 0x0F
BMG160_RANGE_2000 = 0x80
BMG160_RANGE_1000 = 0x81
BMG160_RANGE_500 = 0x82
BMG160_RANGE_250 = 0x83
BMG160_RANGE_125 = 0x84

BMG160_BW_REGISTER = 0x10
BMG160_BW_32 = 0x07
BMG160_BW_64 = 0x06
BMG160_BW_12 = 0x05
BMG160_BW_23 = 0x04
BMG160_BW_47 = 0x03
BMG160_BW_116 = 0x02
BMG160_BW_230 = 0x01
BMG160_BW_523 = 0x00

BMG160_MAIN_POWER_REGISTER = 0x11
BMG160_MAIN_POWER_NORMAL = 0x00
BMG160_MAIN_POWER_SUSPEND = 0x80
BMG160_MAIN_POWER_DEEP_SUSPEND = 0x20

class BMG160():
    def __init__(self, smbus, kwargs = {}):
        self.__dict__.update(kwargs)
        if not hasattr(self, 'address'):
            self.address = BMG160_DEFAULT_ADDRESS
        if not hasattr(self, 'range'):
            self.range = BMG160_RANGE_2000
        if not hasattr(self, 'bandwidth'):
            self.bandwidth = BMG160_BW_23
        self.smbus = smbus

        self.smbus.write_byte_data(self.address, BMG160_RANGE_REGISTER, self.range)
        self.smbus.write_byte_data(self.address, BMG160_BW_REGISTER, self.bandwidth)

    def get_readings(self):
        data = self.smbus.read_i2c_block_data(self.address, BMG160_RATE_X_LSB, 6)
        gyroX = data[0] + (data[1] << 8)
        gyroY = data[2] + (data[3] << 8)
        gyroZ = data[4] + (data[5] << 8)

        if gyroX > 32767:
            gyroX -= 65536
        if gyroY > 32767:
            gyroY -= 65536
        if gyroZ > 32767:
            gyroZ -= 65536
        return {'X': gyroX, 'Y': gyroY, 'Z': gyroY}
