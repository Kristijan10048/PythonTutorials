#!/usr/bin/python

# Example code from YouTube 0:18:23 (http://youtu.be/RrPZza_vZ3w?t=18m23s)
import urllib.request

#open url
u = urllib.request.urlopen('http://aviationweather.gov/adds/metars/index?submit=1&station_ids=LWSK&chk_metars=on&chk_tafs=on&hoursStr=55.2&std_trans=raw')

#read data
data = u.read()

print("Retrieved data");

#open file 
f = open('rt22.xml', 'wb')

#write data in to file
f.write(data);
f.close();

print("Data successfully saved in to file!");
