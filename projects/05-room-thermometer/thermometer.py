"""Project 5: room thermometer (DHT22).

Wiring: DHT22 + -> 3.3V, out -> GPIO4, - -> GND.
Needs `dtoverlay=dht11,gpiopin=4` in /boot/firmware/config.txt and a reboot;
the kernel driver then exposes readings in sysfs, in thousandths.
Read no faster than every 2 seconds. An occasional failed read is normal.
"""

from pathlib import Path
import time


dev = next(Path("/sys/bus/iio/devices").glob("iio:device*"))

def read_dht():
    t = int((dev / "in_temp_input").read_text()) / 1000
    h = int((dev / "in_humidityrelative_input").read_text()) / 1000
    return t, h

while True:
    try:
        t, h = read_dht()
        print(f"{t:.1f} C / {h:.1f} %RH")
    except OSError as e:
        print(e)
        pass
    time.sleep(2.5)
