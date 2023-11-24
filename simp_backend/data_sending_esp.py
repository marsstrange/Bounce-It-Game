# ESP32 connection to the server via SSH, sending humidity data to the server

import network 
import urequests 
import dht 
import machine 
import time 
 
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
 
d = dht.DHT11(machine.Pin(4)) 
 
while(True): 
    time.sleep(1) 
    d.measure() 
    urequests.get(f"http://vps.levandrovskiy.ru:7187/telemetry?temp={d.temperature()}&hum={d.humidity()}")
