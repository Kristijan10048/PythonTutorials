class CApPerson:
	#private members
	__Id = "123";
	
	#public members
	FirstName = "John";
	LastName = "Doe";
	
	#constructors
	def __init__(self):
		print("__Constructor of CApPerson__");
		print("------------------------------------");
	
	#public methods
	def PrintMe(self):
		print("------------------------------------");
		print("First name:{0}\nLast name {1}".format(self.FirstName, self.LastName));
		print("------------------------------------");
		print("Private data: Id{0}".format(self.__Id ));
		
class CApEmployee(CApPerson):
	#Private members

	#Public methods
	JobDescription = "Something to do";
	
	#Constructor with call to base constructor
	def __init__(self):
		super(CApEmployee, self).__init__();
		print("__Constructor of CApEmployee__");
		print("---------------------------------------");
	
	#constructor with jobDescription param
	def __init__(self, jobDescription):
		#/assign vale to job description attribute
		#The call is only on the derived class constructor
		self.JobDescription = jobDescription;	
	
	#Public methods
	def PrintMe(self):
		#call sto base class printMe method
		super(CApEmployee , self).PrintMe();
		print("Job description:  {0}".format(self.JobDescription));

#create new instance of the class
testP = CApPerson();
testP.PrintMe();

#access to private methods
testP.__Id = "Private access";

#set public properties a.k.a class attributes 
testP.FirstName = "Alex";
testP.LastName = "Testovski";
testP.PrintMe();

print("-------------------Create Emplloyee  object----------------------------");
newEmp = CApEmployee("I have no idea what to do");

newEmp.PrintMe();