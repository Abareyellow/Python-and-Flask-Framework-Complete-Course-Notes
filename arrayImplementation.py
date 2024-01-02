# Create a inital Array
arr = [10, 20, 30, 40, 50]
print(arr)

# Call Elements From The Array
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])
print(arr[-5])

# Add Elements To The Array & Get The Length of An Array
brands = ["Coke", "Apple", "Google", "Microsoft", "IBM"]
print(brands)

num_brands = len(brands)
print(num_brands)

brands.append("Toyota")
print(brands)

#Delete Element From Array
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
print(colors)
del colors[4]
print(colors)
colors.remove("blue")
print(colors)
colors.pop(3)
print(colors)

#Change Elements In An Array
fruits = ["Apple", "Mango", "Grapes", "Banana", "Orange"]
print(fruits)
fruits[1] = "Pineapple"
print(fruits)
fruits[-1] = "Guava"
print(fruits)

#Concatanating Arrays
concat = [1, 2, 3]
concat = concat + [4, 5, 6]
print(concat)

# Repeating an Element in An Array
repeat = ["a"]
print(repeat)
repeat = repeat * 5
print(repeat)

#Slicing in Array
fruits2 = ["Apple", "Mango", "Grapes", "Banana", "Orange"]
print(fruits2)
print(fruits2[1:4])
print(fruits2[:3])
print(fruits2[-4:])
print(fruits2[-3:-1])

#Multi-Dimesional Array
multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])