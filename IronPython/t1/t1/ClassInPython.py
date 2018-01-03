#define class
class A:
    #public
    _count =0;
    _size = 12;
    
    #private 
    __private = 0;
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

#crate object from class A
test = A(10,45);

#create object from class B
tB = B(99,90);
tB.Displ();

#set public member
test._count = 33;

#direct acccess
test.__private = 11;


#set from method
test.SetPrvt(123);
test.Displ();