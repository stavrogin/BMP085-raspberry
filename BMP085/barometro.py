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

print "Temperature: %.2f C" % temp
print "Pressure:    %.2f hPa" % (pressure / 100.0)
print "Altitude:    %.2f" % altitude

import time
ts = time.localtime()
print ts
ts = time.mktime(ts)
ts = int(round(ts * 1000))
print ts

currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
print currentTime

row = "%s;%s;%s\n" %(ts,tempCelsius,pressurehPa)
# Scrive un file.
#secondo param: w (scrittura troncando il file se esiste); a+ -> append
out_file = open("rilevazioni.csv","a+")
out_file.write(row)
out_file.close()


#import urllib2
#url = "http://tostao82.appspot.com/tostao82?data=%s" %(row)

#try:
#   connection = urllib2.urlopen(url)
#   print connection.getcode()
#   print connection.geturl()
#   print connection.info()
#   print connection.read()
#   connection.close()
#except urllib2.HTTPError, e:
#   print "no bueno"   
#   print e.code
   
import sqlite3
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

# Drop table
#c.execute("DROP TABLE IF EXISTS WEATHER_DATA")
# Create table
c.execute("CREATE TABLE IF NOT EXISTS WEATHER_DATA ("
			"time DATETIME PRIMARY KEY NOT NULL,"
			"pressure REAL NULL,"
			"temperature REAL NULL,"
			"altitude REAL NULL"
			")")
			
# Larger example that inserts many records at a time
currentWeatherData = [(currentTime, pressurehPa, tempCelsius, altitude)]
c.executemany('INSERT INTO WEATHER_DATA VALUES (?,?,?,?)', currentWeatherData)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
