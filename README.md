# TMP102_Pi
A script for controlling the TMP102 temperature sensor with the Raspberry Pi.  This is a very basic and not at all comprehensive script which was put together quite quickly.

This repo contains three files: TMP102.py which controls the sensor, example.py which show a how to use the script, and readme.md which is this file.

Suggested usage:
- Place TMP102.py in the sample folder as your script, and import it using `import TMP102`.
- use `temperature = TMP102.get_temp()` to store the temperature in degrees C in a variable called `temperature`.

KNOWN ISSUES:

Currently only implements the basic temperature-fetching functionality of the sensor, so this script is very barebones.  It could probably also be a bit more resilient and efficient.  
