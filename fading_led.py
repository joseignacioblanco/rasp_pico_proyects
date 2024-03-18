#--------------------------parpadio------------------------
"""
from machine import Pin,
import time
led_25 = Pin(25,Pin.OUT)
while True:
        led_25.value(1)
        time.sleep(1)
        led_25.value(0)
        time.sleep(1)
        
"""        
#---------------------------fading------------------------------

from machine import Pin, PWM
from time import sleep

#Setup PWM pin
led = machine.Pin(25)
led_pwm = PWM(led)
duty_step = 129 #step size for changing the duty cycle

#set PWM frequency
frequency = 62500
led_pwm.freq(frequency)

try:
    while True:
        #increase the duty cycle gradually
        for duty_cycle in range(0, 65536, duty_step):
            led_pwm.duty_u16(duty_cycle)
            sleep(0.001)
            
        #decrease the duty cycle gradually
        for duty_cycle in range(65536, 0, -duty_step):
            led_pwm.duty_u16(duty_cycle)
            sleep(0.001)
            
except KeyboardInterrupt:
    print("Keyboard interrupt")
    led_pwm.duty_u16(0)
    print(led_pwm)
    led_pwm.deinit()