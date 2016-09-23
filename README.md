# P1X Zero IoT
Raspberry Pi Zero IoT Device (Camera/OLED/Sensors/WiFi)

![P1X Zero IoT - photo](https://i.imgur.com/Us57WzD.jpg)

# Hardware list

- Raspberry Pi Zero
- OLED 128x64 (+ connection cable)
- NoIR Camera Module (+ connection cable)
- WiFi (+ micro-mini adapter)


# Setup

## Raspbian

## I2C

- sudo apt-get install i2c-tools
- sudo usermod -aG i2c pi
- sudo modprobe i2c-dev
- ls -l /dev/i2c*
- i2cdetect -y 1
- remember the ID (my has: 3D)

## OLED

- sudo apt-get update
- sudo apt-get install build-essential python-dev python-pip
- sudo pip install RPi.GPIO 
- sudo apt-get install python-imaging python-smbus
- sudo apt-get install git
- git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
- cd Adafruit_Python_SSD1306
- sudo python setup.py install

## The Script

- p1x-zero-iot.py
