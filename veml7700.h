#include "esphome.h"
#include "Adafruit_VEML7700.h"

class VEML7700Sensor : public PollingComponent, public Sensor {
public:
    Adafruit_VEML7700 veml;
    
    VEML7700Sensor() : PollingComponent(1000) { }
    
    void setup() override {
        veml.begin();
    }
    
    void update() override {
        float lux = veml.readLux();
        publish_state(lux);
    }
};
