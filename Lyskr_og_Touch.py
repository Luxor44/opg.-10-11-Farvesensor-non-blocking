import time
from machine import TouchPad, Pin

r_led = Pin(17, Pin.OUT)
r_prev_time = 0
r_interval = 100
r_state = 0
r = TouchPad(Pin(27))

while True:
    r_currentTime = time.ticks_ms()
    if (r.read() < 200 and r_currentTime - r_prev_time > r_interval ):
        r_prev_time = r_currentTime
        if r_state == 1:
            r_state = 0
        else:
            r_state = 1
        r_led.value(r_state)
        r_start_time = time.ticks_ms()