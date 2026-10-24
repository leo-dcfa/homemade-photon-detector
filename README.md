# homemade-photon-detector

A homelab fun project I'm working on: learning electronics on a Raspberry Pi 5, one small circuit at a time. It starts with blinking an LED and works up through buttons and sensors. Each folder under `projects/` is one self-contained script, and each one builds on the last.

## Progress

| # | Project | What it covers | Status |
|---|---------|----------------|--------|
| 1 | [Blink an LED](projects/01-blink/blink.py) | GPIO output, LED polarity, current-limiting resistors | Done |
| 2 | [Button-controlled LED](projects/02-button-led/button_led.py) | GPIO input, events | Done |
| 3 | [Pedestrian crossing](projects/03-pedestrian-crossing/crossing.py) | Sequencing, gpiozero composite devices | Done |
| 4 | [Breathing LED](projects/04-breathing-led/breathing.py) | PWM and duty cycle | Done |
| 5 | [Room thermometer](projects/05-room-thermometer/thermometer.py) | DHT22 through the kernel driver and sysfs | Done |
| 6 | [Distance meter](projects/06-distance-meter/distance.py) | HC-SR04 echo timing, noisy readings | In progress |

## Hardware

- Raspberry Pi 5 (16 GB) with the active cooler
- Breadboard, jumper wires, 5 mm LEDs and 220–330 Ω resistors
- Push-button modules (signal, VCC, GND)
- DHT22 temperature and humidity sensor
- HC-SR04 ultrasonic distance sensor, 3.3 V version

## Pin map

BCM (GPIO) numbers, not physical pin positions. Run `pinout` on the Pi to see the header.

| GPIO | Used for |
|------|----------|
| 4 | DHT22 data |
| 17 | Red LED (the single LED in projects 1, 2 and 4) |
| 22 | Yellow LED |
| 23 | Green LED |
| 24 / 25 | HC-SR04 Echo / Trig |
| 27 | Button |

Power the button modules and sensors from the 3.3 V pin. The Pi's GPIO pins are 3.3 V only.

## Running

On the Pi:

```sh
git clone https://github.com/leo-dcfa/homemade-photon-detector.git
cd homemade-photon-detector
uv venv --system-site-packages   # gpiozero and lgpio come preinstalled with Raspberry Pi OS
uv run projects/01-blink/blink.py
```

Without uv, use `python3 -m venv --system-site-packages .venv` and run scripts with `.venv/bin/python`.

Project 5 reads the DHT22 through the kernel driver, so it needs this line in `/boot/firmware/config.txt`, followed by a reboot:

```
dtoverlay=dht11,gpiopin=4
```

The `dht11` driver handles the DHT22 too.

## Pi 5 notes

- `RPi.GPIO` doesn't work on the Pi 5, so everything here uses `gpiozero`. Most older tutorials use `RPi.GPIO`.
- The Pi has no analog inputs, so analog parts need an ADC or an I2C module.
