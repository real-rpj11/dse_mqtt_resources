# Precy Jane Roxas

from microbit import *
import paho.mqtt.client as mqtt

circle = Image("09990:90009:90009:90009:09990")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        display.show(Image.YES)
        client.subscribe("joy")
    else:
        display.show(Image.NO)

def on_message(client, userdata, msg):
    # print(msg.payload.decode())
    if msg.payload.decode() == "C":
        display.show(circle)
        pass
    elif msg.payload.decode() =="N":
        display.show(Image.ARROW_N)
    elif msg.payload.decode() =="S":
        display.show(Image.ARROW_S)
    elif msg.payload.decode() == "W":
        display.show(Image.ARROW_W)
    elif msg.payload.decode() == "E":
        display.show(Image.ARROW_E)
    elif msg.payload.decode() == "SE":
        display.show(Image.ARROW_SE)
    elif msg.payload.decode() == "SW":
        display.show(Image.ARROW_SW)
    elif msg.payload.decode() == "NE":
        display.show(Image.ARROW_NE)
    elif msg.payload.decode() == "NW":
        display.show(Image.ARROW_NW)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()