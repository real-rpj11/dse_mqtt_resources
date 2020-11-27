from adafruit_clue import clue
import paho.mqtt.client as mqtt

def display_text(data):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*clue.acceleration)
    clue_data[1].text = "Gyro: {} {} {} dps".format(*clue.gyro)
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*clue.magnetic)
    clue_data[3].text = "Pressure: {} hPa".format(clue.pressure)
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {} C".format(data)
    clue_data[6].text = "Humidity: {} %".format(data)
    clue_data[7].text = "Proximity: {}".format(clue.proximity)
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
    clue_data.show()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clue_sliders")
        display_text(0)
    if rc == 1:
        client.subscribe("clue_slider")
        display_text(1)



def on_message(client, userdata, msg):
    display_text(int(msg.payload.decode()))
    print(int(msg.payload.decode()))

clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()