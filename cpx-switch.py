# Precy Jane Roxas
from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt


# connect to the broker
def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("switches")
    if rc == 1:
        cp.red_led = True
        client.subscribe("switches")
    if rc == 2:
        cp.red_led = True
        client.subscribe("switches")

# Called when a message has been received on a topic that the client 
# subscribes to and the message does not match an existing topic filter callback
def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "true":
        cp.pixels[0] = (255, 255, 255)
    elif  msg.payload.decode() == "false":
        cp.pixels[0] = (0, 0, 0)

    elif msg.payload.decode() == "true1":
        cp.pixels[1] = (255, 255, 255)
    elif msg.payload.decode() == "false1":
        cp.pixels[1] = (0, 0, 0)

    elif msg.payload.decode() == "true2":
        cp.pixels[2] = (255, 255, 255)
    elif msg.payload.decode() == "false2":
        cp.pixels[2] = (0, 0, 0)

    

        
cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt