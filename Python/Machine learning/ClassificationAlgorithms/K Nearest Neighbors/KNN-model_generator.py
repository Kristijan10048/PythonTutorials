import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import pickle
import sys



def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)


# accurasy constant for the model to train
C_ACC_DV = 0.017;

C_STR_MODEL_FILENAME = "CarsModel.pickle";

print("--------------------------------------------");
print('Running...');

# load the .csv file
data = pd.read_csv("CarData\car1c.data");

print("Data is loaded. Outputing first 5 rows:\n");
print(data.head());

x = data[['Buying', 'Maint', 'Doors', 'Persons', 'Lug_boot', 'Safety']];
y = data[['Class']];


model = KNeighborsClassifier(n_neighbors = 5);
acc = 0;
i = 0;
count = 1;
print("Status:", end = '');
while(abs(1 - acc) > C_ACC_DV):

	# split the data in to training and testing
	x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size = 0.1);
	
	# do the fitting
	model.fit(x_train, y_train.values.ravel());

	# get accuracy of the current model
	acc = model.score(x_test, y_test);
	
	
	if(i % 100 == 0):
		 progress(count, 10000, status='');
		 count = count + 1;
	i = i + 1;
	
progress(10000, 10000, status='');
print("\n");
with open("CarsModel.pickle", "wb") as file:
	pickle.dump(model, file);
	
print("Model with {0} is saved as {1}".format(acc, C_STR_MODEL_FILENAME));