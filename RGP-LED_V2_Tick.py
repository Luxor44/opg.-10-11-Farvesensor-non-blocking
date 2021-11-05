from machine import Pin, PWM
import time

frequency = 5000
start_duty = 1023
r = PWM(Pin(18), frequency, start_duty)
g = PWM(Pin(5), frequency, start_duty)
b = PWM(Pin(19), frequency, start_duty)

while True:
    for duty_cycle in range(1023):
        r.duty(duty_cycle)
        print("r", duty_cycle)
        time.ticks_ms(20)
