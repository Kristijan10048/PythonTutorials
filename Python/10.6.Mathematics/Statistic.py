#!/usr/bin/python
import statistics


def DemoStatistic(dataParam):

	#calculate mean
	mean = statistics.mean(dataParam);

	#calculate median
	median = statistics.median(dataParam);

	#calculate standard deviation
	stdv = statistics.variance(dataParam);

	#count values outside 3 sigma range
	noiseCount = 0;
	for value in dataParam:
		if value < (-3* stdv) + mean or value > (3*stdv) + mean:
			#print(" %.4f" %(value));
			noiseCount += 1;

			
	print("-----------------Simple------------------------");
	print("Data length: %d" %(len(dataParam)) );
	print("Values outside 3sigma: %d" %(noiseCount) );
	print("Mean: %.7f" %(mean));
	print("Median: %.7f"%(median));
	print("Standard deviation: %.7f"%(stdv));
	print("------------------------------------------------");


#Simple data
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5];
DemoStatistic(data);	

#open file for reading with temperature readings from LM335Z analog sensor 
fileName = "temp_readings_with_kalman.txt";
txtFile = open(fileName, 'r');


data1 = [];
data1K =[];
for line in txtFile:
	#print("Line :", line);
	
	#split data in two cols
	buffer= line.split(" ");
	
	data1.append( float(buffer[0]) );
	data1K.append( float(buffer[1]) );
	
#close the text file
txtFile.close();


#statistics for temp data
DemoStatistic(data1);

#statistics for temp data with kalman filter	
DemoStatistic(data1K);	