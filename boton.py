from machine import Pin
from time import sleep
read = Pin(16, Pin.IN)
while True:
    if read.value() == 1:
        print('La lectura fue 1 o verdadero')
    else:
        print('La lectura fue 0 o falso')
    sleep(0.5)