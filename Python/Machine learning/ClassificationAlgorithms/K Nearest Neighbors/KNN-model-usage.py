import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import pickle
import sys
from enum import Enum

# Enums for file coumns
class Buying(Enum):
	Vhigh = 14;
	High = 13;
	Med = 12;
	Low = 11;

class Maint(Enum):
	Vhigh = 14;
	High = 13;
	Med = 12;
	Low = 11;

class Doors(Enum):
	One = 1;
	Two = 2;
	Three = 3;
	Four = 4;
	More  = 599;

class Persons(Enum):
	Two = 2;
	Four = 4;
	More = 99;

class LugBoot(Enum):
	Low = 11;
	Med = 12;
	Big = 15;
	
class Safety(Enum):
	Low = 11;
	Med = 12;
	Big = 15;
	
class CarState(Enum):
	Unacceptable = 21;
	Acceptable = 22;
	Good = 23;
	Vgood = 24;
	

C_STR_MODEL_FILENAME = "CarsModel.pickle";
# loaded_model; 
with open(C_STR_MODEL_FILENAME, 'rb') as file:
	
	# load the model from disk
	loaded_model = pickle.load(file);
	print("Model loaded successfully...");
print(loaded_model);

# Atributes order in .csv file:
# 	Buying, Maint, Doors, Persons, Lug_boot, Safety,Class
x = [[Buying.Med.value, 
	  Maint.High.value,
	  Doors.More.value,
	  Persons.More.value,
	  LugBoot.Big.value,
	  Safety.Big.value]];

print(x);	

# execute predictio from loaded model
res = loaded_model.predict(x);

print("Result numerical value is {0} and state is: {1}".format(res[0], CarState(res)));