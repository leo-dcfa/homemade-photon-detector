"""Two-player reaction game.

Wiring: LED on GPIO17 through a resistor (as in blink). Button modules:
player 1 signal -> GPIO5, player 2 signal -> GPIO6, both VCC -> 3.3V and
GND -> GND. The LED lights after a random delay; the first press wins.
"""

from gpiozero import LED, Button
from random import uniform
from time import sleep, monotonic

led = LED(17)
p1 = Button(5, pull_up=None, active_state=True)
p2 = Button(6, pull_up=None, active_state=True)

while True:
    sleep(uniform(2, 5))
    led.on()
    start = monotonic()
    while not (p1.is_pressed or p2.is_pressed):
        pass
    winner = "Player 1" if p1.is_pressed else "Player 2"
    print(f"{winner} wins: {(monotonic() - start) * 1000:.0f} ms")
    led.off(); sleep(2)
