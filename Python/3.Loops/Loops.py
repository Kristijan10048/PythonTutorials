#!/usr/bin/env python

#******************************
#			For loop
#******************************
print("---------For loop-------------\n");
for letter in 'Python':
   print('Current Letter :', letter);
   
#******************************
#		For loop with break
#******************************
print("---------For loop with break-------------\n");
for letter in 'Python':
   if letter == 'h':
      break
   print('Current Letter :', letter);

#******************************
#		For each C# like
#******************************
print( "---------For each loop-------------\n");

#declare array with numbers
numbers = [1,2,3,4,5,6,7];

for number in numbers:
    print("Current number in the array is", number);
	
#******************************
#		For with range
#******************************
print("---------For loop and len function-------------\n");
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print('Current fruit :', fruits[index])

print("---------For loop 0 to n-------------\n");
for x in range(0, 3):
    print("We're on time %d" % (x))
   
   
#******************************
#		While loop
#******************************
print("---------While loop-------------\n");
count = 10;
i=0;
while(i<count):
    i+=1;
    print("i = ", i);