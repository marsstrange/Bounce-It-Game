# Case 4
# The system should have the following features:
# 1. The system should receive values from the soil moisture sensor. 
# The readings are published on the MQTT server in the topic /class/stand<id>/humidity, where <id> is the number of the case with laboratory equipment.
# 2. Watering is performed at a low humidity level (sensor readings less than 15) and is accompanied by sending the message "watering" to the topic /class/stand<id>/pump, 
# where <id> is the number of the case with laboratory equipment. It should be possible to start the pump forcibly (perform watering), 
# upon receipt of the message "do" in the corresponding topic.
# 3. The power supply to the submersible pump is carried out using a mini-relay module or a power key.
import network
import urequests
from umqtt.robust import MQTTClient
import time
import onewire
import dht
import machine

d = dht.DHT11(machine.Pin(21))
d.measure()
print(d.temperature())

def cb(topic, msg):
    print('Subscribe: Received Data: Topic = {}, Msg = {}\n'.format(topic, msg))

ssid = "IoT_Case"
password = "qweqweqwe"
station = network.WLAN(network.STA_IF)
if station.isconnected() == True:
    print("Already connected")
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print("Connection successful")
print(station.ifconfig())

mqtt_server = 'io.adafruit.com'
client_id = "13312sdsa213aasdw"
client = MQTTClient(client_id=client_id, server=mqtt_server,user="cupOfLungo",password="aio_vKzu0104LFgKopj8kOLTy4aa504b")
client.connect() 
client.set_callback(cb) # second thread 
client.subscribe("cupOfLungo/feeds/doWatering")
print("Connection successful")
# client.publish("cupOfLungo/groups/HumSens/json",json.dumps({"feeds":{"temp":25,"hum":54}}))
while True:
    temr = d.temperature()
    client.publish("cupOfLungo/feeds/humiditys", str(d.humidity()))
    if d.humidity() < 53:
         client.publish("cupOfLungo/feeds/pump", "watering")
         time.sleep(3)
    # print(client.check_msg())
    # time.sleep(3)
    if client.check_msg() == "Subscribe: Received Data: Topic = b'cupOfLungo/feeds/doWatering', Msg = b'do'":
         client.publish("cupOfLungo/feeds/pump", "wateringDO")
         time.sleep(3)
