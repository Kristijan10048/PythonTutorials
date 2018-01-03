import sys;
import clr;
import re;

#result = re.match(pattern, string)
m = re.search('(?<=abc)def', 'abcdef')
print m.group(0);

line = "Cats are smarter than dogs";
line2 = "test of some tests in test"

matchObj = re.match( 'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"
print "done!"

regExStr = "(\d+)";
text = "456";
test = """triple""";

m11 = re.match(text, regExStr, re.IGNORECASE);

if m11 is not None:
    if m11.group(0) is not None:
        print m11.group(0);
    else:
        print "Nothing";


regExStr = "\<(test[0-9](\.\d+)?)\>"
text = "<test3>"


m1 = re.match(text, regExStr, re.IGNORECASE);

if m1 is not None:
    if m1.group(0) is not None:
        print m1.group(0);
    else:
        print "Nothing";
        