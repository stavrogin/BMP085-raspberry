#!/usr/bin/python

import time
ts = time.time()
ts = int(round(time.time() * 1000))
print ts

import datetime
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
print st