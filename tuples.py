# Creating an empty tuple:
tuple1 = ()
print(tuple1)

#creating tuples with integer elements:
tuple2 = (1, 2, 3)
print(tuple2)

# tuple with mixed datatypes:
tuple3 = (101, "Anirban", 20000.00, "HR Dept")
print(tuple3)

#creation of nested tuple
tuple4 = ("points", [1, 4, 3], (7,8,6))
print(tuple4)

#tuple can be created without any parentheses
# also called tuple packing
tuple5 = 101, "Anirban", 20000.00, "HR Dept"
print(tuple5)

empid, empname, empsal, empdept = tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)

print(type(tuple5))

#accessing elements in a tuple
tuple1 = ('w', 'e','l','c','o','m','e')
print(tuple1)
print(tuple1[1])
print(tuple1[3])
print(tuple1[5])

#nested tuple
nested_tuple = ("point", [1,3,4], (5,6,7))
print(nested_tuple)
print(nested_tuple[0][3])
print(nested_tuple[1][2])
print(nested_tuple[2][2])

# slicing tuple contents
tuple1 = ('w', 'e','l','c','o','m','e')
print(tuple1[1:3])
print(tuple1[:-3])
print(tuple1[3:])
print(tuple1[:])

# concatenation of tuples
tuple2 = ('w', 'e', 'l')
tuple3 = ('c', 'o', 'm', 'e')
print(tuple2)
print(tuple3)
print(tuple2 + tuple3)

print(("again", ) * 4)

# tuple methods
tuple5 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple5.count('e'))
print(tuple5.index('c'))

# membership
print('c' in tuple5)
print('c' not in tuple5)
print('a' in tuple5)
print('a' not in tuple5)

# iteration through tuple elements
for letters in tuple5:
  print("letter is -> ", letters)

# built-in function with tuple
tuple6 = (22, 33, 55, 44, 77, 66, 11)
print(tuple6)

print(max(tuple6))
print(min(tuple6))
print(sorted(tuple6))
print(len(tuple6))