#import smbus for i2c communications
import smbus
import time
#import the chip library
import bmg160

# Get I2C bus, this is I2C Bus 1
bus = smbus.SMBus(1)
#kwargs is a Python set that contains the address of your device as well as desired range and bandwidth
#refer to the chip's datasheet to determine what value you need for range and bandwidth to suit your project
#The default address for this chip is 0x68, this simply allows you to manually set it for multi-board chains. 
kwargs = {'address': 0x68, 'range': 0x80, 'bandwidth': 0x04}
#create the BMG160 object from the BMG160 library and pass it the kwargs and com bus.
#the object requires that you pass it the bus object so that it can communicate and share the bus with other chips/boards if necessary
bmg160 = bmg160.BMG160(bus, kwargs)

while True :
    #print out the readings.
    #the readings will be return in a set keyed X, Y, and Z for the corresponding values
    print bmg160.take_reading()
    #this sleep is not required
    time.sleep(.25)
