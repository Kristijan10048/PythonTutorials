from sklearn import tree;
from sklearn.ensemble import RandomForestClassifier;
from sklearn.linear_model import LogisticRegression;
from sklearn.svm import SVC;
import time;

# Site: https://towardsdatascience.com/how-to-build-a-gender-classifier-in-python-using-scikit-learn-13c7bb502f2e
# We are going to use four classifiers provided by scikit-learn. They are:
# decision tree
# random forest
# logistic regression
# Support Vector Classifier (SVC)

# Data 
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], 
     [154, 54, 37], [166, 65, 40], [190, 90, 47], 
	 [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], 
     [181, 85, 43], [168, 75, 41], [168, 77, 41]];

Y = ['male', 'male', 'female', 
	 'female', 'male', 'male', 
	 'female',
	 'female','female', 'male', 
	 'male', 'female', 'female'];
	 
	 
# Test data	 
test_data = [[190, 70, 43], [191, 85, 43], [191, 95, 43], [154, 75, 38],[181,65,40]];
test_labels = ['male','female','male'];

startTime = 0;
# Util methods
def PrintAlgoName(name):
	print("Running {}...".format(name));

def StopwatchStart():
	global startTime;	
	startTime = time.time();
	 
def StopwatchStop():
	global startTime;
	endTime = time.time();
	elapsed = endTime - startTime;
	print("Execution time is: {0}".format(elapsed));
	startTime = 0;


# Random Forest Classifier
def RandomForestClassifierMethod():
	print("------------------------------------------");
	PrintAlgoName("RandomForestClassifierMethod");
	StopwatchStart();
	rfc_clf = RandomForestClassifier(n_estimators  = 150 );

	rfc_clf.fit(X, Y);

	rfc_prediction = rfc_clf.predict(test_data);

	StopwatchStop();
	print("Random Forest Classifier {0}".format(rfc_prediction));
	print("------------------------------------------");
	
#LogisticRegression
def LogisticRegressionClassifier():
	print("------------------------------------------");
	PrintAlgoName("LogisticRegressionClassifier");
	StopwatchStart();
	
	l_clf = LogisticRegression(solver = "lbfgs");
	l_clf.fit(X,Y);
	
	l_prediction = l_clf.predict(test_data);		
	print("LogisticRegression classifier: {0}".format(l_prediction));
	
	StopwatchStop();
	print("------------------------------------------");

def DecisionTreeClassifier():
	print("------------------------------------------");
	PrintAlgoName("DecisionTreeClassifier");
	StopwatchStart();

	#create an instance
	dtc_clf = tree.DecisionTreeClassifier();

	#do the fitting
	dtc_clf = dtc_clf.fit(X, Y);

	# calculate prediction
	dtc_prediction = dtc_clf.predict(test_data);

	print("Decision tree classifier: {0}".format(dtc_prediction));
	StopwatchStop();
	print("------------------------------------------");

#Support Vector Classifier
def SVCMethod():
	print("------------------------------------------");
	PrintAlgoName("SVCMethod");
	StopwatchStart();
	
	s_clf = SVC();
	s_clf.fit(X,Y);
	s_prediction = s_clf.predict(test_data);
	
	print("SVC classifier: {0}".format(s_prediction));
	StopwatchStop();
	print("------------------------------------------");
	
# DecisionTreeClassifier
DecisionTreeClassifier();

# Random Forest Classifier
RandomForestClassifierMethod();

# LogisticRegression
LogisticRegressionClassifier();

# Support Vector Classifier
SVCMethod();