// This #include statement was automatically added by the Particle IDE.
#include "BMG160.h"

BMG160 sensor;

void setup() {
    sensor.init();
    Particle.variable("gyroX", sensor.gyroX);
    Particle.variable("gyroY", sensor.gyroY);
    Particle.variable("gyroZ", sensor.gyroZ);
}

void loop() {
    sensor.loop();
}
