"""Distance meter (HC-SR04).

Wiring: VCC -> 3.3V, Trig -> GPIO25, Echo -> GPIO24, GND -> GND.
This is the 3.3V version of the sensor, so no voltage divider is needed.
Readings jitter by 1-2 cm; aim at a flat, hard surface.
"""

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=25, max_distance=2)
while True:
    print(f"{sensor.distance * 100:.1f} cm")
    sleep(0.2)
