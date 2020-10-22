"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground import cp
from time import sleep
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("cloud")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "on":
        cp.pixels[0] = (255, 255, 255)
    else:
        cp.pixels[0] = (0, 0, 0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# while True:
#     cp.pixels[0] = (255, 255, 255)
#     sleep(1)
#     cp.pixels[0] = (0, 0, 0)
#     sleep(1)
#     # start your code here
#     # pass


# Broker for online client in github
# wss://mqtt.eclipse.org:443/mqtt