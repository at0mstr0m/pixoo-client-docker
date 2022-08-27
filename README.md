# pixoo-client-docker

Fork of [Divoom Pixoo client for Python3](https://github.com/virtualabs/pixoo-client).
Only tested on Raspberry Pi 3 Model B. Requires Docker.

## Getting Started

1. Connect to **Divoom Timebox-Evo** via Bluetooth
    1. Use [Bluez](http://www.bluez.org/) via `sudo bluetoothctl`
    2. Then use 
        ```
        agent on 
        default-agent
        scan on
        ```
    3. Wait until your device appears on the list. Then you can turn off scanning with `scan off`
    4. Establish Bluetooth connection to your Divoom Timebox-evo
        ```
        trust DEVICE_MAC_ADDRESS
        pair DEVICE_MAC_ADDRESS
        ```
        If an error appears use `remove DEVICE_MAC_ADDRESS` and retry establishing a connection.
    5. Use `exit` to exit the configuration.
2. Build Docker image:
`docker build --platform linux/arm/v7 --tag pixoo-api .`
`docker build --platform linux/arm/v7 -t gui-react .`
3. Save to .tar-File:
`docker save pixoo-api > pixoo-api.tar`
`docker save gui-react > gui-react.tar`
4. Load image on Raspberry Pi:
`docker load --input IMAGE_NAME.tar`
5. Run on Raspberry Pi 3 Model B with network from host to use bluetooth device:
`docker run -tid --network=host -e MAC_ADDRESS="DEVICE_MAC_ADDRESS" pixoo-api`
`docker run -tid --network=host gui-react`

---
## Original README:

This small python script provides a way to communicate with a Divoom Pixoo over Bluetooth. 

This script provides a class able to manage a Pixoo, but you need to create your own code to make it work.

## Dependencies

Use a third-party software to bind your computer with your pixoo (BlueZ + blueman-applet for instance).
Then you may use this python class to manage your Pixoo.

## How to use this class

This class provides many methods to connect and manage a Pixoo device.

* `connect()̀`: creates a connection with the device and keeps it open while the script is active
* `draw_pic()`: draws a picture (resized to 16x16 pixels) from a PNG file
* `draw_anim()`: displays an animation on the Pixoo based on a GIF file (16x16 pixels)
* `set_system_brightness`: set the global brightness to a specific level (0-100)

---

## Image sources:

[pong.gif](https://giphy.com/gifs/3o7btZzyj3zGh20SSk)
Pixel Art Numbers inspired by and taken from [here](http://pixelartmaker.com/art/cb56ff285ad38b3).