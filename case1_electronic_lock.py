import machine 
import time 
from collections import OrderedDict 
 
led = machine.Pin(2,machine.Pin.OUT) 
reley_pin = machine.Pin(21, machine.Pin.OUT) 
 
b1 = machine.Pin(16, machine.Pin.IN) 
b2 = machine.Pin(18, machine.Pin.IN) 
b3 = machine.Pin(5, machine.Pin.IN) 
b4 = machine.Pin(17, machine.Pin.IN) 
 
prev = 0 
flag = 0 
 
# code = [2,1,4,4,3] 
code = [2] 
entered = [0,0,0,0,0] 
liste = [] 
 
def isPressed(): 
    if not b1.value(): 
        return 1 
    if not b2.value(): 
        return 2 
    if not b3.value(): 
        return 3 
    if not b4.value(): 
        return 4 
    else:  
        return 0 
     
def bulb(): 
    time.sleep(1) 
    led.value(not led.value()) 
 
def rel(): 
    reley_pin.on() 
    time.sleep(3) 
    reley_pin.off() 
 
while True: 
    # print(b1.value(), b2.value(), b3.value(), b4.value()) 
    # print(isPressed()) 
    curr = isPressed() 
 
    if curr and (prev != curr): 
        liste.append(isPressed()) 
     
    prev = curr 
    print(liste) 
    time.sleep(0.1) 
 
    if code == liste: 
        for i in range(0,2): 
            reley_pin.on() 
            bulb() 
        reley_pin.off() 
 
        print("OK") 
    else: 
        led.value(True)
