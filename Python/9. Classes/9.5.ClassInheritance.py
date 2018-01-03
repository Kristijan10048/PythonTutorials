#define class
class Person:
	
	#Public Members
	_FirstName	= "";
	_LastName = "";
	
	#Private Members
	__privateData
	
	def __init__(self, FirstName, LastName)
		print("Constructor:", Person);
		self._FirstName = FirstName;
		self._LastName = LastName;
	

class Employee (Person):

    #public
    _count = 0;
    _size = 1;
    
    #private 
    __employmentDdate = 0;
	
    #constructor
    def __init__(self, count, size):
        print("Constructor A");
        self._count = count;
        self._size = size;        

    #print class members
    def Displ(self):
        print(self._count);
        print(self._size);
        print(self.__private);

    #access private member
    def SetPrvt(self, value):
        self.__private = value;

class B(A):
    _bsize = -1;
    _fsize = -1;

    def __init__(self, bsize, fsize):
       print("Init B");
       self._bsize=bsize;
       self._fsize=fsize;
