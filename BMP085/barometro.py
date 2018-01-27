#!/usr/bin/python

from Adafruit_BMP085 import BMP085

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

temp = bmp.readTemperature()
pressure = bmp.readPressure()
altitude = bmp.readAltitude()

if temp < 0 :
	temp = bmp.readTemperature()
if pressure < 0 :
	pressure = bmp.readPressure()
if altitude < 0 :
	altitude = bmp.readAltitude()

tempCelsius = temp
pressurehPa = pressure / 100.0
altitudem = altitude

import time
currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
currentWeatherData = [(currentTime, pressurehPa, tempCelsius, altitude)]

print "Temperature: %.2f C" % tempCelsius
print "Pressure:    %.2f hPa" % pressurehPa
print "Altitude:    %.2f" % altitudem

