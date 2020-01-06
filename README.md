# gaia

Gaia is a custom built environment sensor. This repository contains:
- parts list
- wiring diagram
- required software and setup instructions

## Parts List

The parts list can be found in the `parts.xlsx` file.

## Hardware and Wiring

TODO

## Overview of Operation

A single Python script `run.py` manages collecting and uploading of data.

Sensors are connected via I2C and current state is reported via MQTT.

This script is run at startup by the systemd `gaia.service`, which can be found in this repository.

## Install and Configure Raspbian

1. Flash Raspian Lite image to SD card

	https://www.raspberrypi.org/downloads/raspbian/
	
2. Enable SSH (create empy file at root of file system called `ssh`)

`touch /Volumes/boot/ssh`

3. Add wifi network configuration
	- Create file
	`touch /Volumes/boot/wpa_supplicant.conf`
	- Add following
    ```
    country=AU
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="NETWORK NAME"
        psk="PASSWORD"
    }
    ```

## Tune Boot Performance (Optional)

Ideas from http://himeshp.blogspot.com/2018/08/fast-boot-with-raspberry-pi.html

1. Edit `/boot/config.txt` and add the following:

```
# Disable the rainbow splash screen
disable_splash=1

# Disable bluetooth 
dtoverlay=pi3-disable-bt
 
# Overclock the SD Card from 50 to 100MHz
# This can only be done with at least a UHS Class 1 card 
dtoverlay=sdtweak,overclock_50=100
 
# Set the bootloader delay to 0 seconds. The default is 1s if not specified. 
boot_delay=0

# Overclock the raspberry pi. This voids its warranty. Make sure you have a good power supply.
force_turbo=1
```

2. Edit kernel boot flags in /boot/cmdline.txt
	1. Set `fsck.repair=no`
	2. Add `quiet` command

e.g. `dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=32e07f87-02 rootfstype=ext4 elevator=deadline fsck.repair=no quiet rootwait`

3. Disable wait for network

``sudo raspi-config``

4. Disable unused services

```
sudo systemctl disable dphys-swapfile.service
sudo systemctl disable keyboard-setup.service
sudo systemctl disable apt-daily.service
sudo systemctl disable hciuart.service
sudo systemctl disable avahi-daemon.service
sudo systemctl disable triggerhappy.service
sudo systemctl disable bluetooth.service
```

## Install Software

1. Set timezone and hostname

`sudo raspi-config`

2. Download software
```
curl -LO https://github.com/sjtrny/gaia/archive/master.zip
unzip -d gaia master.zip
```
3. Run setup
This will automatically install dependencies, requirements etc and start the poseidon service
```
cd gaia
sudo ./setup.sh
```
