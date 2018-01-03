import clr;
import sys;
import System;
from System import Array;

clr.AddReference("System.Core")

#import linq
clr.ImportExtensions(System.Linq);

#create array of integers
numbers = Array[int]([5,4,3,7,8]);


tmp = Array[int](range(100));

print "Before sorting :" , numbers;

#array sort
Array.Sort(numbers);
print "Sortting :", numbers;
print "Element access:", numbers[1];

strArray = Array[str](["Test1", "Test2", "Test3"]);
print "String at pos 1: ", strArray[1];

reals = Array[float]([0.0, 0.3, 0.4]);
print "Real numbers:", reals;

#Check for available methods in list
print dir(list);