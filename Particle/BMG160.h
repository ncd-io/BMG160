#include "spark_wiring_i2c.h"
#include "spark_wiring_constants.h"

//Starting point for reading out data
#define BMG160_RATE_X_LSB 0x02

#define BMG160_RANGE_REGISTER 0x0F
#define BMG160_RANGE_2000 0x80
#define BMG160_RANGE_1000 0x81
#define BMG160_RANGE_500 0x82
#define BMG160_RANGE_250 0x83
#define BMG160_RANGE_125 0x84

#define BMG160_BW_REGISTER 0x10
#define BMG160_BW_32 0x07
#define BMG160_BW_64 0x06
#define BMG160_BW_12 0x05
#define BMG160_BW_23 0x04
#define BMG160_BW_47 0x03
#define BMG160_BW_116 0x02
#define BMG160_BW_230 0x01
#define BMG160_BW_523 0x00

#define BMG160_MAIN_POWER_REGISTER 0x11
#define BMG160_MAIN_POWER_NORMAL 0x00
#define BMG160_MAIN_POWER_SUSPEND 0x80
#define BMG160_MAIN_POWER_DEEP_SUSPEND 0x20

class BMG160{
public:
    void init();
    void setAddress(int a0);
    
    void loop();
    
    void takeReading();
    void sendCommand(int reg, int data);
    void readBytes(int reg, int *bytes, int length);
    
    int address = 0x68;
    
    int range = BMG160_RANGE_2000;
    int bandwidth = BMG160_BW_23;
    
    int last_checked = 0;
    
    int gyroX;
    int gyroY;
    int gyroZ;
};
