# Libraries
from machine import Pin
from time import sleep

# Pin definitions
b1 = Pin(36, Pin.IN)
b2 = Pin(39, Pin.IN)
b3 = Pin(34, Pin.IN)
b4 = Pin(35, Pin.IN)
b5 = Pin(32, Pin.IN)
b6 = Pin(33, Pin.IN)
b7 = Pin(25, Pin.IN)
b8 = Pin(26, Pin.IN)

# Variables
numero = 0

# Main loop
while True:
    if b1.value() == 1:
        numero += 1
    if b2.value() == 1:
        numero += 2
    if b3.value() == 1:
        numero += 4
    if b4.value() == 1:
        numero += 8
    if b5.value() == 1:
        numero += 16
    if b6.value() == 1:
        numero += 32
    if b7.value() == 1:
        numero += 64
    if b8.value() == 1:
        numero += 128
    print("Valor decimal: ", numero)
    sleep(0.5)
    numero = 0