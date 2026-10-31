"""Project 8: parking sensor.

Wiring: the project 3 LEDs (red -> GPIO17, yellow -> GPIO22, green -> GPIO23,
each through a resistor) and the project 6 HC-SR04 (VCC -> 3.3V,
Trig -> GPIO25, Echo -> GPIO24, GND -> GND).
Green means clear (over 50 cm), yellow means slow, red means stop (20 cm or less).
"""

from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(echo=24, trigger=25, max_distance=2)
green, yellow, red = LED(23), LED(22), LED(17)

while True:
    cm = sensor.distance * 100
    green.value = int(cm > 50)
    yellow.value = int(20 < cm <= 50)
    red.value = int(cm <= 20)
    sleep(0.1)
