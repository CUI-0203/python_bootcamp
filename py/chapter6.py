#Lists

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

#Accessing Elements
print(fruits[0])  # "apple"
print(fruits[-1]) # "cherry"
print(numbers[1:4]) # [2, 3, 4]
print(numbers[:3]) # [1, 2, 3]
print(numbers[2:]) # [3, 4, 5]


fruits.append('orange')   # add to end
fruits.insert(1,"blueberry")  #Insert at Index
fruits.remove("apple")   #Remove by Value
popped = fruits.pop()   #Remove and Return Last Element
fruits.sort()   #sort in place
fruits.reverse()   #reverse in place

# List operations
len(fruits)   #Length
"apple" in fruits   # check membership
fruits = ["mango"]   #Concatenation
fruits * 2  #Repetition

print(len(fruits))

#exe
groceries = ["vegetables" , "cheese", "bread"]
print(groceries)
groceries.append("eggs")
print(groceries)
groceries.remove("cheese")
print(groceries)

#exe2.
numbers = [5, 8, 30, 15, 23,19,3]
print("largest:", max(numbers))
print("smallest:", min(numbers))
