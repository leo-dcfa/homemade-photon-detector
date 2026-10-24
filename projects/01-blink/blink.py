"""Project 1: blink an LED.

Wiring: GPIO17 -> 330 Ω resistor -> LED long leg; LED short leg -> GND.
"""

from gpiozero import LED
from signal import pause

led = LED(17)
led.blink(on_time=0.5, off_time=0.5)
pause()
