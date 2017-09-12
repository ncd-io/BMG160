#include "BMG160.h"
#include "Particle.h"

void BMG160::init(){
    if(!Wire.isEnabled()){
        Wire.begin();
    }
    sendCommand(BMG160_RANGE_REGISTER, range);
    sendCommand(BMG160_BW_REGISTER, bandwidth);
}

void BMG160::setAddress(int a0){
    address |= a0;
}

void BMG160::loop(){
    int now = millis();
    if(now-last_checked > 1000){
        last_checked = now;
        takeReading();
    }
}

void BMG160::takeReading(){
    int data[6];
    readBytes(BMG160_RATE_X_LSB, data, 6);
    gyroX = data[0] + (data[1] << 8);
    gyroY = data[2] + (data[3] << 8);
    gyroZ = data[4] + (data[5] << 8);
    
    if(gyroX > 32767) gyroX -= 65536;
    if(gyroY > 32767) gyroY -= 65536;
    if(gyroZ > 32767) gyroZ -= 65536;
}

void BMG160::sendCommand(int reg, int cmd){
    Wire.beginTransmission(address);
    Wire.write(reg);
    Wire.write(cmd);
    Wire.endTransmission();
}

void BMG160::readBytes(int reg, int *bytes, int length){
    Wire.beginTransmission(address);
    Wire.write(reg);
    Wire.endTransmission();
    Wire.requestFrom(address, length);
    for(int i=0;i<length;i++){
        bytes[i] = Wire.read();
    }
}
