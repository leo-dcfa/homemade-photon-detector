"""Slide dimmer: an LED's brightness follows a PiicoDev slide potentiometer.

Wiring: the slider plugs into the PiicoDev adapter, which uses I2C
(SDA -> GPIO2, SCL -> GPIO3). The LED goes from the adapter's TX pin
(GPIO14) through a resistor to GND, as in blink. I2C must be on;
`i2cdetect -y 1` shows the slider's address.
"""

from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from gpiozero import PWMLED
from time import sleep

LED_PIN = 14          # the adapter's TX pin is GPIO14

pot = PiicoDev_Potentiometer()   # reads 0-100
led = PWMLED(LED_PIN)

while True:
    value = pot.value
    led.value = value / 100      # 0 = off, 1 = full brightness
    print(f"\r{value:5.1f}", end="", flush=True)
    sleep(0.02)
