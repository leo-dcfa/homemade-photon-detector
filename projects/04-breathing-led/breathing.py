"""Project 4: breathing LED with PWM.

Wiring: same as project 1 (GPIO17 -> resistor -> LED -> GND).
"""

from gpiozero import PWMLED
from signal import pause

led = PWMLED(17)
led.pulse(fade_in_time=1.5, fade_out_time=1.5)
pause()
