#!/usr/bin/env python

#------------------------------------------
#	Dictionary declaration "key:value"
#------------------------------------------
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#access elements
print("----------------------------");
print("dict['Name']: ", dict['Name']);
print("dict['Age']: ", dict['Age']);
print("----------------------------");

#change value
dict['Age']=12;
print("dict['Age']: ", dict['Age']);

#delete element in dict
del dict['Class'];

#Access keys
print("----------------------------");

#print("Dict keys:", dict.keys);
for key, value in dict.items():
	print("Key: {0} Value: {1}.".format(key, value));	

#Access keys only
print("----------------------------");

#print keys from dictionary
print("Keys:",)
for key in dict.keys():
	print("Key:", key);

#print keys from dictionary	
for value in dict.values():
	print("Value: {0}".format(value));

# printable dictionary
print("----------------------------");
print(str(dict));
	
#delete dictionary
del dict ; # delete entire dictionary
