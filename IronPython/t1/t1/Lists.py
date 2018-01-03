# Creatin lists
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

# Accessing Values in Lists
print "------------Accessing Values in Lists-------------\n";
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

#Update lists
print "------------------Update lists--------------------\n";
list = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]

for value in list:
    print "List :", value;

#Delete List Elements
print "------------------Delete List Elements--------------------\n";
print list;

#delete element on postion 1
del list[1];

#print the list again after element has been deleted
print list;

print "List length:", len(list)
scalar = 10;
v1 = [1, 2, 3];
v2 = [4, 5, 6];
v3 = v1 + v2;
v4 = scalar *v2
print "list add :", v3;
print "List * scalar" , v4;