import machine
import time
from machine import TouchPad, Pin
red = machine.Pin(16, machine.Pin.OUT)
yellow = machine.Pin(17, machine.Pin.OUT)
green = machine.Pin(15, machine.Pin.OUT)
interval = 100
led_state = 0
led_state2 = 0
led_state3 = 0
previousTime = 0
Touch_state = 0
Touch_state2 = 0
Touch_state3 = 0
Touch = TouchPad(Pin(4))
Touch2 = TouchPad(Pin(0))
Touch3 = TouchPad(Pin(2))
#16,17,15
while True:
    Touch_currentTime = time.ticks_ms()
    
    if (Touch.read() < 200 and Touch_currentTime - previousTime > interval):
        previousTime = Touch_currentTime
        print("TouchMebabe")
        if led_state == 1:
            led_state = 0
            machine.Pin(16, machine.Pin.OUT, value=1)
        else:
            Touch_state = 1
            red.value(Touch_state)
            Touch_start_time = time.ticks_ms()
            machine.Pin(16, machine.Pin.OUT, value=0)
        
    if (Touch2.read() < 200 and Touch_currentTime - previousTime > interval):
        previousTime = Touch_currentTime
        print("TouchMeBabe2")
        if led_state2 == 1:
            led_state2 = 0
            machine.Pin(17, machine.Pin.OUT, value=1)
        else:
            Touch_state2 = 1
            yellow.value(Touch_state2)
            Touch2_start_time = time.ticks_ms()
            machine.Pin(17, machine.Pin.OUT, value=0)
            
    if (Touch3.read() < 200 and Touch_currentTime - previousTime > interval):
        previousTime = Touch_currentTime
        print("TouchMebabe3")
        if led_state3 == 1:
            led_state3 = 0
            machine.Pin(15, machine.Pin.OUT, value=1)
        else:
            Touch_state = 1
            green.value(Touch_state3)
            Touch3_start_time = time.ticks_ms()
            machine.Pin(15, machine.Pin.OUT, value=0)