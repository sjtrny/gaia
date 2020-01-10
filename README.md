# gaia

Gaia is a custom built environment sensor. This repository contains:
- parts list
- required software and setup instructions

## Overview

Gaia provides the following data:
- Ambient Lux
- Temperature
- Humidity
- Pressure
- Gas Resistance (Air Quality)

Two I2C sensor are used to collect this data:
- VEML770 (ambient lux)
- BME680 (everything else)

Gaia runs on [ESPHome](https://esphome.io). See `gaia.yml`  for the configuration of the device.

## VEML7700 Support

ESPHome does not have native support for the VEMl7700 device, so I have written a small device wrapper `veml7700.h`, which leverages the "Adafruit VEML7700 Library".

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

3. Plug in ESP32 via USB

4. Compile and upload to ESP32

```
		esphome gaia.yml run
```