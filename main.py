import time
import paho.mqtt.client as mqtt

from sensors.dht11 import read_dht
from sensors.bh1750 import read_bh1750

from aktoren.licht import light_on, light_off
from aktoren.heizung import heater_on, heater_off
from aktoren.fenster import open_window, close_window
from aktoren.ventilation import fan_on, fan_off

def befehl(client, msg):

    topic = msg.topic
    payload = msg.payload.decode()

    print(f"{topic}: {payload}")

    # Lichtsteuerung
    if topic == "home/bedroom/light/set":
        if payload == "ON":
            light_on()
            client.publish("home/bedroom/light/state", "ON")
        elif payload == "OFF":
            light_off()
            client.publish("home/bedroom/light/state", "OFF")

    # Heizungssteuerung
    elif topic == "home/hall/heater/set":
        if payload == "ON":
            heater_on()
            client.publish("home/hall/heater/state", "ON")
        elif payload == "OFF":
            heater_off()
            client.publish("home/hall/heater/state", "OFF")

    # Ventilationssteuerung
    elif topic == "home/basement/fan/set":
        if payload == "ON":
            fan_on()
            client.publish("home/basement/fan/state", "ON")
        elif payload == "OFF":
            fan_off()
            client.publish("home/basement/fan/state", "OFF")

    # Rolladensteuerung
    elif topic == "home/kitchen/blinds/set":
        if payload == "OPEN":
            open_window()
            client.publish("home/kitchen/blinds/state", "OPEN")
        elif payload == "CLOSE":
            close_window()
            client.publish("home/kitchen/blinds/state", "CLOSE")

# MQTT client Setup
client = mqtt.Client()
client.on_message = befehl
client.connect("localhost", 1883)
client.loop_start()

# Abbonieren auf Control Topics
client.subscribe("home/bedroom/light/set")
client.subscribe("home/hall/heater/set")
client.subscribe("home/basement/fan/set")
client.subscribe("home/kitchen/blinds/set")

print("HA started")

# Publish Sensor Data
while True:
    temp, hum = read_dht()
    lux = read_bh1750()

    client.publish("home/hall/temperature", temp)
    client.publish("home/basement/humidity", hum)
    client.publish("home/bedroom/lightlevel", lux)

    time.sleep(0.5)