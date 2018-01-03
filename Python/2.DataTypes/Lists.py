#!/usr/bin/env python

#define list
squares = [1, 4, 9, 16, 25];

#define another list
cubes = [1, 8, 27, 65, 125];

for elem in cubes:
	print("Element: %d \n" %(elem));

# add the cube of 6
cubes.append(216)

# and the cube of 7
cubes.append(7 ** 3)

#prints full list
print("Accessing lists")
print("Cubes:",cubes);

#print first 3 elements
print("elements from position 0 (included) to 3\n");
print("Cubes:",cubes[0:3])

#print first 3 elements
print("elements from position 0 (included) to 3\n");
print("Cubes:",cubes[:3])

#print first 3 elements
print("elements from position 3 (included) to end\n");
print("Cubes:",cubes[3:])

#access second elements
print("Cubes[1]=",cubes[1]);