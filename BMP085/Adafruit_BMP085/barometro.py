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
#https://www.raspberrypi.org/forums/viewtopic.php?p=479204#p479204
#pressure increases roughly 110 every 100m, altitude is calculated at the sea level
altitude = bmp.readAltitude(pressure + 700)

#if relevations go wrong..
if temp < 0 :
	temp = bmp.readTemperature()
if pressure < 0 :
	pressure = bmp.readPressure()
if altitude < 0 :
	altitude = bmp.readAltitude(pressure + 700)

tempCelsius = temp
pressurehPa = pressure / 100.0
altitudem = altitude

import time
currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
currentWeatherData = [(currentTime, pressurehPa, tempCelsius, altitude)]

print "Temperature: %.2f C" % tempCelsius
print "Pressure:    %.2f hPa" % pressurehPa
print "Altitude:    %.2f m" % altitudem


import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': "application/json"
}

body = {
	"altitude": altitudem,
	"temperature": tempCelsius,
	"pressure": pressurehPa,
	"datasourceId": 1
}

import json
try:
	response = requests.post('http://192.168.1.23:8080/meteo/weatherdata', headers=headers, data=json.dumps(body))
	print response.status_code
	print response.text
except:
	print "Error: maybe host 192.168.1.23 is unreachable..."

try:
	response = requests.post('http://192.168.1.24:8080/meteo/weatherdata', headers=headers, data=json.dumps(body))
	print response.status_code
	print response.text
except:
	print "Error: maybe host 192.168.1.23 is unreachable..."

