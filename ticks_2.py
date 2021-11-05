import machine
from time import ticks_ms, sleep

led = machine.Pin(17, machine.Pin.OUT)
interval = 100
led_state = 0
previousTime = 0

while True:
    currentTime = ticks_ms()
    print(currentTime - previousTime)
    
    if (currentTime - previousTime > interval):
        previousTime = currentTime
        print("in if")
    if led_state == 1:
        led_state = 0
    else:
        led_state = 1
        led.value(led_state)