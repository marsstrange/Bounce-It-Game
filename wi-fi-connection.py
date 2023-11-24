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
# print(urequests.get("https://goweather.herokuapp.com/weather/Bryansk").json())

mqtt_server = 'io.adafruit.com'
client_id = "13312sdsa213aasdw"
client = MQTTClient(client_id=client_id, server=mqtt_server,user="cupOfLungo",password="aio_vKzu0104LFgKopj8kOLTy4aa504b")
client.connect() 
# client.set_callback(cb)
# client.subscribe("#")
print("Connection successful")
# client.publish("cupOfLungo/groups/HumSens/json",json.dumps({"feeds":{"temp":25,"hum":54}}))
while True:
    temr = d.temperature()
    # client.check_msg()
    client.publish("cupOfLungo/feeds/HumSens", str(d.temperature()))
    time.sleep(3)


