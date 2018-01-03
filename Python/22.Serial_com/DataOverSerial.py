#!/usr/bin/python

import datetime;
import time;
import serial;
import re;
from time import sleep;

#serial port settings
C_STR_COM_PORT = 'COM3';
C_INT_BAUD_RATE = 115200;


#NMEA
C_INT_PITOT_DIFF_PRESSURE = 0 ;#in Pa

#blue fly vario #WRONG!!!
C_STR_NMEA_FMT = "BFV,{0},{1},{2},{3},{4}";

C_STR_NMEA_OPEN_VARIO_FMT = "POV,{0},{1}";

def OpenAndInitSerialPort ():
	
	#Open serial port	
	ser = serial.Serial();

	ser.port = C_STR_COM_PORT
	
	ser.baudrate = C_INT_BAUD_RATE

	#number of bits per bytes
	#.bytesize = serial.EIGHTBITS 

	#set parity check: no parity
	#ser.parity = serial.PARITY_NONE 

	#number of stop bits
	#ser.stopbits = serial.STOPBITS_ONE

	#ser.timeout = None
	ser.timeout = 0            

	#timeout block read
	#ser.timeout = 2             

	#disable software flow control
	#ser.xonxoff = False     

	#disable hardware (RTS/CTS) flow control
	#ser.rtscts = False     

	#disable hardware (DSR/DTR) flow control
	#ser.dsrdtr = False 

	#timeout for write
	ser.writeTimeout = 120	
	
	ser.open();
	
	return ser;

def  ReadFromSerial(port):
	#read first 40 lines
	i = 0;
	while(True):
		raw_data = port.readline();
		
		#convert bytes to string
		#sData = raw_data.decode("utf-8");
		print(raw_data);
		
		i += 1;

def WriteOpenVarioData(serialPort):
	#S: true airspeed in km/h
	# Example: $POV,S,123.45*05
	#Pressure

	#  P: static pressure in hPa
	# Example: $POV,P,1018.35*39
  
	# Q: dynamic pressure in Pa
	# Example: $POV,Q,23.3*04
  
	# R: total pressure in hPa
	#Example: $POV,R,1025.17*35
	#Temperature

	#T: temperature in deg C
	#  Example: $POV,T,23.52*35
	#Voltage

	# V: battery voltage in V
	#Example: $POV,V,11.99*1A        
	#Vario

	#  E: TE vario in m/s
	#  Example: $POV,E,2.15*14
	
	#km/h
	airspeed = 34; 
	
	static_pres = 1018;
	#in hPa	
	total_pres = 1012;
	#in C deg
	temp = 34;
	bat_voltage = 8.9;
	vario =1.2;
	
	currInstr = C_STR_NMEA_OPEN_VARIO_FMT.format("S", airspeed);
	
	#Add check sum
	data_str = "$POV,S,123.45*05\n\r";	#AddCheckSum(currInstr);	 
	print(data_str);
		
	serialPort.write(bytes(data_str.encode()));
	#sleep(1000);
	
	#currInstr = C_STR_NMEA_OPEN_VARIO_FMT.format("R", total_pres);
	
	#Add check sum
	#data_str =	AddCheckSum(currInstr);	 
	#print(data_str);
		
	#serialPort.write(data_str.encode('ascii'));
	#sleep(1000);
	
	#currInstr = C_STR_NMEA_OPEN_VARIO_FMT.format("E",vario);
	
	#Add check sum
	#data_str = AddCheckSum(currInstr);	 
	#print(data_str);
		
	#serialPort.write(data_str.encode('ascii'));
	#sleep(1000);
		
def AddCheckSum(sentence):
	
	#P: static pressure in hPa
	#Example: $POV,P,1018.35*39
  
	#Q: dynamic pressure in Pa
	#Example: $POV,Q,23.3*04
  
	#R: total pressure in hPa
	#Example: $POV,R,1025.17*35
	#Temperature

	#T: temperature in deg C
	#Example: $POV,T,23.52*35

    # Remove any newlines
	if re.search("\n$", sentence):
		sentence = sentence[:-1];

	if(sentence[0] == '$'):
		sentence = sentence[:-1];
		
	nmeadata = sentence; # cksum = re.split('\$', sentence)
	#print("NMEA DATA:"+nmeadata);

	calc_cksum = 0
	for s in nmeadata:
		calc_cksum ^= ord(s)

	#Return the nmeadata, the checksum from
	#sentence, and the calculated checksum
	chk_str =  hex(calc_cksum)[2:];
	str = "${0}*{1}\n\r".format(nmeadata, chk_str);
	return str.upper();
		

try:
	serialP = OpenAndInitSerialPort();
	
	print("Connected to Serial Port:" + C_STR_COM_PORT);
	
	#ReadFromSerial(serialP);
	
	#"$BFV,pressure(Pa),vario(cm/s), temp(deg C), battery(%),pitotDiffPressure(pa)*checksum\r\n
	# For  e.g. BFV,1012,1, 25, 15,0  With checksum $BFV,1012,1, 25, 15,0*7E

	vario = 0; 
	pres = 1012;
	temp = 34;
	bat = 23;
	i =0;
	
	ver = "BFV 9\n\r";
	while(True):		
		WriteOpenVarioData(serialP);
		print("Step:{0}".format(i));
		sleep(0.1);
		i += 1;
		#create  NMEA string
		#currInstr = C_STR_NMEA_FMT.format(pres, vario, temp, bat, C_INT_PITOT_DIFF_PRESSURE);
		#print(currInstr);
	
		#Add check sum
		#data_str =	AddCheckSum(currInstr);
	 
		#print("Data string:"+data_str);
		
		#serialP.write(ver.encode());
		#sleep(1);
		
		#write data on serial port
		#serialP.write(data_str.encode());	
		
		
		#test = "PRS 17CBA\n\r";
		#serialP.write(test.encode());
		#delay for 1 ms
		#sleep(1);
except OSError as err:
	print('Data could not be written: {0}'.format(err));	
	#serialP.close();


#serialP.close();
print("Serial port %s closed. Exiting..."%(C_STR_COM_PORT));
