"""Toggle an LED with a button.

Wiring: the blink LED on GPIO17, plus a button module with
signal -> GPIO27, VCC -> 3.3V, GND -> GND. The module outputs HIGH when
pressed; if presses feel reversed, set active_state=False.
"""

from gpiozero import LED, Button
from signal import pause

led = LED(17)
btn = Button(27, pull_up=None, active_state=True)
btn.when_pressed = led.toggle
pause()
