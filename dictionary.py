# Accessing elements from a dictionary
new_dict = {1: "Hello", 2:"Hi", 3:"Hola"}
print(new_dict)
print(new_dict[1])
print(new_dict.get(2))

# Updating value
new_dict[1] = "Hey"
print(new_dict)

# ADdding value
new_dict[4] = "Bonjour"
print(new_dict)

# Creating a new dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)

# remove a particular item
print(squares.pop(4))
print(squares)

# remove an arbitrary item
print(squares.popitem())
print(squares)

del squares[1]

print(squares)

squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)

# remove all item
squares.clear()
print((squares))