#Accessing Values in Strings
print "---------------Accessing Values in Strings--------------\n";
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

#Appending Strings
print "----------------Appending strings------------------------\n"
var1 = 'Hello World!'
print "Updated String :- ", var1[:6] + 'Python'
tmpStr = "Yahoo"
tmpStr += var1;
print tmpStr

#format strings
print "-------------------Format strings------------------------\n"
#Format Symbol	Conversion
#   %c	character
#   %s	string conversion via str() prior to formatting
#   %i	signed decimal integer
#   %d	signed decimal integer
#   %u	unsigned decimal integer
#   %o	octal integer
#   %x	hexadecimal integer (lowercase letters)
#   %X	hexadecimal integer (UPPERcase letters)
#   %e	exponential notation (with lowercase 'e')
#   %E	exponential notation (with UPPERcase 'E')
#   %f	floating point real number
#   %g	the shorter of % f and %e
#   %G	the shorter of % f and %
print 'X: %d, Y: %0.3f Z: % 0.1f' %(12, 0.999, 113.12345);

#Unicode String
print "---------------Unicode String---------------\n"
print u'Hello, world!'
t= "test 1234"
print t[-1];

#Triple Quotes
print "---------------Triple Quotes---------------\n"
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str