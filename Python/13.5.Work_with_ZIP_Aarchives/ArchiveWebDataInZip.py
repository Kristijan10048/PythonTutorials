#!/usr/bin/env python

#imports
import math
import urllib.request, datetime
import zipfile


#constants
C_STR_DATE_TIME_FMT = "{0}-{1}-{2}_{3}_{4}_{5}";

C_STR_URL_TO_OPEN = "http://aviationweather.gov/adds/metars/index?submit=1&station_ids=LWSK&chk_metars=on&chk_tafs=on&hoursStr=55.2&std_trans=raw";

#----------------------------------------------------------------------------
#Returns string for current date and time
#	Parameters:
#		-None
#----------------------------------------------------------------------------
def DateTimeToString():
	#get current date and time
	time = datetime.datetime.now();
	
	#return formatted date and time
	tmp = C_STR_DATE_TIME_FMT.format(time.year, time.month, time.day, time.hour, time.minute, time.second);
	return  tmp;

#open url
u = urllib.request.urlopen(C_STR_URL_TO_OPEN);

#read data
data = u.read();

#null is none in Python
#check for data
if(data is not None):
	print("Received  data....");
	
	#get curren date time string
	currDateAndTime = DateTimeToString();
	
	fileName = currDateAndTime + "-log.xml";
	
	try:
		#open the file
		f = open(fileName, 'wb');
	
		#write url data in to file
		f.write(data);
	
		#close the file
		f.close();
				
		myZip = zipfile.ZipFile('Archive.zip', mode='w');
		
		
		myZip.write(fileName);
		myZip.close();
	except OSError as err:
		print("Error:", err);
		print("Error in creating file:", fileName);
