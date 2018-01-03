#!/usr/bin/env python
import math
#---------------------------
#	declare string
#---------------------------
str = "test";
print(str);

print("-----------------\n");

#---------------------------
#	Access character in the string. 
#	Zero based
#---------------------------
print("str[2]=",str[2]);

print("-----------------\n");
print("str[2]=",str[1:]);

#---------------------------
#	Append string
#---------------------------
str += " testovski";
print("str=", str);

#---------------------------
#	String length
#---------------------------
print("-----------------\n");
print("Length:", len(str));

#---------------------------
#	Replace character
#---------------------------
#str[len(str) -1] = "I"; Don't!


#---------------------------
#	String format
#---------------------------
print("-----------------\n");

#print floats with decimal places
pi = math.pi;
print("Pi:%5.3f\n" %(pi));

print("Pi:%5.7f" %(pi));
print("Pi:%.7f" %(pi));

#---------------------------
#	C# string format
#---------------------------
print("First value is {0}. Second is : {1}.".format(10, 12));

#Another	String	forming	example	
ip	=	"192.168.1.1"	
mac	=	"AA:BB:CC:DD:EE:FF"	
print("The gateway has the following IP: %s	and	MAC: %s addresses"	%(ip,	mac));

#---------------------------
#	C# Split string
#---------------------------
print("-----------------\n");
logFile="/var/log/messages";

buffer = logFile.split("/");

print("Buffer elements:", buffer);
print("Buffer[1]:", buffer[1]);

#---------------------------
#	String	Concatenation
#---------------------------
print("-----------------\n");
userName	=	"ali";
domainName	=	"ashemery.com";
userEmail	=	userName	+	"@"	+	domainName;

print(userEmail);

