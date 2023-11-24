from machine import ADC, Pin
from machine import I2C
import time
from machine import SoftI2C

amp_adc = ADC(Pin(35), atten = ADC.ATTN_11DB)
mic_led_adc = ADC(Pin(33), atten = ADC.ATTN_11DB)

prev_left = amp_adc.read_uv()/1000000
prev_right = mic_led_adc.read_uv()/1000000

led = Pin(5,Pin.OUT)
led_2 = Pin(18,Pin.OUT) 

# sdaPIN= Pin(21)
# sclPIN= Pin(18)

# I2C_ADDR = 0x60 #device hex, hex(device) method
# totalRows = 8
# totalColumns = 8

# i2c=I2C(sda=sdaPIN, scl=sclPIN, freq=10000)   
# lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns) #connection object

# devices = i2c.scan()
# if len(devices) == 0:
#  print("No i2c device !")
# else:
#  print('i2c devices found:',len(devices))
# for device in devices:
#  print("At address: ",hex(device))

while True:
    time.sleep(0.1)
    curr_left = amp_adc.read_uv()/1000000
    curr_right = mic_led_adc.read_uv()/1000000

    #TODO CENTRE
    if curr_left - prev_left > 1.5:
        led.value(not led.value()) 
        print('LEFT')
        led(1)
        time.sleep(0.1)
        led(0)
    if curr_right - prev_right > 0.5:
        print('RIGHT')
        led_2(1)
        time.sleep(0.1)
        led_2(0)
    
    print('Left: ', amp_adc.read_uv()/1000000, 'Right: ', mic_led_adc.read_uv()/1000000)
    time.sleep(0.1)
