#!/usr/bin/python

import datetime;


 #get current date
dateNow =  datetime.date.today();
print("Today's date %s, " %str(dateNow) );


tmpNow = datetime.datetime.now();
print("Current date and time using str method of datetime object: %s" %str(tmpNow) );


time = datetime.datetime.now();

#print("time:", str(time));

print("Time now %s/%s/%s %s:%s:%s" %(time.year, time.month, time.day, time.hour, time.minute, time.second));

#print ("hh:mm:ss format = %s:%s" % (time.hour,  time.second) )
#print("", dateNow);