import sys;
import clr;
#load hash table
from System.Collections import Hashtable;
#HybridDictionary
from System.Collections.Specialized import HybridDictionary;
from System.Collections.Specialized import StringCollection;

#create object
print "---------------Hashtable------------"
m_hashTbl = Hashtable();

m_hashTbl["a"] = "t1";
m_hashTbl["b"] = "t2";
m_hashTbl["d"] = "t3";

for key in m_hashTbl.Keys :
    print "hash value :", m_hashTbl[key];


#string collection
print "---------------String Collections------------"
strBuffer = StringCollection()

strBuffer.Add("abc");
strBuffer.Add("def");
strBuffer.Add("Alpha");

for str in strBuffer :
    print "string :", str;