#***all about range()***
#syntax: range(start, stop, step)
#using range()
for i in range(5):
    print(i)
# range(start,stop)
for i in range(1,5):  #start,stop-1
    print(i)

# range(start,stop,step)
for i in range(1,10,2):
    print(i)

# negative step (Descending order)
for i in range(10,0,-1):
    print(i)

# range() with list()
numbers=list(range(5))
print(numbers)

# works for iterations also
for i in range(3):
    print("Hello")

# length of range()
r=range(1,6)
print(len(r))

# checking membership in range()
print(3 in range(1,5))
print(50 in range(1,15))

# range() with enumerate()
fruits={"apple","banana","cherry"}
for i in enumerate(fruits):
    print(i)

# range in list comprehension
square=[x**2 for x in range(5)]
print(square)

