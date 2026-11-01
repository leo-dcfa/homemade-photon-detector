"""Pedestrian crossing.

Wiring: red LED -> GPIO17, yellow -> GPIO22, green -> GPIO23 (each through a
resistor), button -> GPIO27. The lights sit on green until someone presses
the button.
"""

from gpiozero import TrafficLights, Button
from time import sleep

lights = TrafficLights(red=17, amber=22, green=23)
btn = Button(27, pull_up=None, active_state=True)

while True:
    lights.green.on()
    btn.wait_for_press()
    lights.green.off(); lights.amber.on(); sleep(2)
    lights.amber.off(); lights.red.on(); sleep(5)
    lights.red.off()
