# gaia

Gaia is a custom built environment sensor. This repository contains:
- parts list
- required software and setup instructions

## Overview

Gaia provides the following data:
- Ambient Lux
- Local Temperature (near device)
- Local Humidity
- Local Pressure
- Local Gas Resistance (Air Quality)
- Remote Temperature (away from device)

Two I2C sensor are used to collect this data:
- VEML770 (ambient lux)
- BME680 (local readings)
- DS18B20 waterproof (remote temp)

Temperature and Humidity are displayed on an Adafruit LCD.

Gaia runs on [ESPHome](https://esphome.io). See `gaia.yml`  for the configuration of the device.

## AdaFruit RGB LCD Shield

ESPHome does not have an official component for the AdaFruit RB LCD Sheild so I have written a component
for it which you can find in the `custom_components`  folder.

## VEML7700 Support

ESPHome does not have an official component for the VEMl7700 device, so I have written a small device wrapper `veml7700.h`, which leverages the "Adafruit VEML7700 Library".

## Parts List

The parts list can be found in the `parts.xlsx` file.

## Hardware and Wiring

TODO

## Instructions

1. Create virtual environment and install dependencies

```
./setup.sh
```

2. Activate virtual environment

```
source venv/bin/activate
```

3. Add wifi details to  `gaia.yml`

4. Plug in ESP32 via USB

5. Compile and upload to ESP32

```
		esphome gaia.yml run
```
