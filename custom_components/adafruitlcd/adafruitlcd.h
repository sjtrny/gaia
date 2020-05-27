#pragma once

#include "esphome/core/component.h"
#include "esphome/core/defines.h"
#include "esphome/core/log.h"
#include "Adafruit_RGBLCDShield.h"

namespace esphome {
    namespace adafruitlcd {
        
        class AdafruitLCDComponent;
        
        
        class AdafruitLCDComponent : public PollingComponent {
        public:
            Adafruit_RGBLCDShield lcd;
            
            void set_writer(std::function<void(AdafruitLCDComponent &)> &&writer) {
                this->writer_ = std::move(writer);
                
            }
            
            void setup() override {
                lcd = Adafruit_RGBLCDShield();
                lcd.begin(16, 2);
                lcd.print("Adafruit LCD");
            }
            
            void update() override {
                if (this->writer_ != 0) {
                    this->writer_(*this);
                }
            }
            
            void clear(){
                lcd.clear();
            }
            
            void print(const char *str) {
                lcd.clear();
                lcd.print(str);
            }
            
            void print(const char *str, int col, int row) {
                lcd.setCursor(col, row);
                lcd.print(str);
            }
            
        protected:
            std::function<void(AdafruitLCDComponent &)> writer_ = 0;
            
        };
        
    }
}


