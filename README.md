# homemade-photon-detector

A homelab fun project I'm working on: building a homemade photon detector on a Raspberry Pi 5. I'm starting with the foundations, learning the electronics one small circuit at a time.

## Foundations

Warm-up circuits, grouped by the Pi interface they use. Each folder holds one self-contained script.

### GPIO

Plain digital pins: on/off outputs, button inputs, PWM and pulse timing.

| Project | What it covers | Status |
|---------|----------------|--------|
| [Blink an LED](foundations/gpio/blink/blink.py) | GPIO output, LED polarity, current-limiting resistors | Done |
| [Button-controlled LED](foundations/gpio/button-led/button_led.py) | GPIO input, events | Done |
| [Pedestrian crossing](foundations/gpio/pedestrian-crossing/crossing.py) | Sequencing, gpiozero composite devices | Done |
| [Breathing LED](foundations/gpio/breathing-led/breathing.py) | PWM and duty cycle | Done |
| [Room thermometer](foundations/gpio/room-thermometer/thermometer.py) | DHT22 through the kernel driver and sysfs | Done |
| [Distance meter](foundations/gpio/distance-meter/distance.py) | HC-SR04 echo timing, noisy readings | Done |
| [Two-player reaction game](foundations/gpio/two-player-reaction-game/game.py) | Timing, polling vs events, game state | Done |
| [Parking sensor](foundations/gpio/parking-sensor/parking.py) | Thresholds, mapping sensor data to LEDs | Done |

### I2C (SDA / SCL)

Two shared wires that talk to sensor chips, each chip at its own address.

| Project | What it covers | Status |
|---------|----------------|--------|
| [Slide dimmer](foundations/i2c/slide-dimmer/dimmer.py) | I2C addresses, `i2cdetect`, analog control without an ADC | In progress |

## Hardware

- Raspberry Pi 5 (16 GB) with the active cooler
- Breadboard, jumper wires, 5 mm LEDs and 220–330 Ω resistors
- Push-button modules (signal, VCC, GND)
- DHT22 temperature and humidity sensor
- HC-SR04 ultrasonic distance sensor, 3.3 V version
- PiicoDev slide potentiometer and a PiicoDev adapter for the Pi

## Pin map

BCM (GPIO) numbers, not physical pin positions. Run `pinout` on the Pi to see the header.

| GPIO | Used for |
|------|----------|
| 2 / 3 | I2C SDA / SCL (PiicoDev slider) |
| 4 | DHT22 data |
| 5 / 6 | Reaction game buttons |
| 14 | Slide dimmer LED (TX on the PiicoDev adapter) |
| 17 | Red LED, and the single LED in the one-LED circuits |
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
uv run foundations/gpio/blink/blink.py
```

Without uv, use `python3 -m venv --system-site-packages .venv`, install the dependencies from `pyproject.toml`, and run scripts with `.venv/bin/python`.

The room thermometer reads the DHT22 through the kernel driver, so it needs this line in `/boot/firmware/config.txt`, followed by a reboot:

```
dtoverlay=dht11,gpiopin=4
```

The `dht11` driver handles the DHT22 too.

The slide dimmer needs I2C turned on: `sudo raspi-config` → Interface Options → I2C.

## Pi 5 notes

- `RPi.GPIO` doesn't work on the Pi 5, so everything here uses `gpiozero`. Most older tutorials use `RPi.GPIO`.
- The Pi has no analog inputs, so analog parts need an ADC or an I2C module.
