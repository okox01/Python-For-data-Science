#***Loop Basics***
# syntax:
    # for variable in iterable:
    #      code to be executed
# For loop :
# using Range()
for i in range(3):
    print(i)
# while loop :
# syntax:
    # while condition:
    #      code block

# using while loop:
i=0
while i<5:
    print(i)
    i+=1

# Nested loops :
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Looping through different data structure:
# 1. List
fruits = ['apple', 'banana', 'cherry']
for index,value in enumerate(fruits):
    print(index,value)

# 2. Tuple
fruits = ('apple', 'banana', 'cherry')
for index,value in enumerate(fruits):
    print(index,value)

# 3. Set
fruits = {'apple', 'banana', 'cherry'}
for index,value in enumerate(fruits):
    print(index,value)
print("\n")
# 4. dictionary
fruits={1:"apple",2:"banana",3:"cherry"}
for index,value in fruits.items():
    print(index,value)


# Else clause in loops:
for i in range(5):
    print(i)
else:
    print("loop completed")

# loop optimization tips:
# 1. Use for loop instead of while loop
# 2. Use range() function instead of len() function
# 3. Use enumerate() function instead of index variable
# 4. Use list comprehension instead of for loop
# 5. Use set data structure instead of list data structure
# 6. Use dictionary data structure instead of list data structure
# 7. Use map() function instead of for loop

# 4. Use list comprehension instead of for loop
square=[x**2 for x in range(5)]
print(square)

# 3. Use enumerate() function instead of index variable
for index,value in enumerate(["a","b","c"]):
    print(index,value)

# use zip() for parallel iterations
names=["Alice","Bob"]
ages=[25,30]
country=["USA","UK"]
for nm,ag,cn in zip(names,ages,country):
    print(nm,ag,cn)


# code example 

# gives two oranges as the loop breaks
squares = ['orange', 'orange', 'purple', 'blue ','orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)

# gives three oranges as the loop does not break
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = [color for color in squares if color == 'orange']
print(new_squares)



    