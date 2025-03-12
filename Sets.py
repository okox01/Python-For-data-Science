#***Creating Set***
#Method:1-> using {}
my_set={1,2,3,4}
print(my_set)
#Method:2-> using set()
my_set2=set(["apple","banana","cherry"])
print(my_set2)
#Method:3->Empty Set
# disclaimer: {}->creates empty dictionary
#            set() -> creates empty set
my_set3=set()
print(type(my_set3))

#***Accessing Set Elements***
#No indexing in sets
#we can access elements using for loop
my_set={1,2,3,4,5,6,7,8,9}
for i in my_set:
    print(i,end=" ")
print("\n")
print(2 in my_set)
print(100 in my_set)

#***Adding elements to set***
#Method:1-> using add()
s={1,2,3,4}
s.add(5)
print(s)
#Method:2-> using update()
p=set([5,8,9,10])
p.update([6,10,12])
print(p)

#***Removing elements from set***
#Method:1-> using remove()->Raises KeyError if element is not present
s={1,2,3,4,5,6,7,8,9}
s.remove(5)
print(s)
#Method:2->using discard()->No error if element not found
s2={1,2,3,4,5,6,7}
s2.discard(5)
print(s2)
#Method:3->using pop()->Removes random element
s3={1,2,3,4,5,6,7,8,9}
p=s3.pop()
print(s3, p)
#Method:4->using clear()->Removes all elements
s4={1,2,3,4,5,6,7,8,9}
s4.clear()
print(s4)

#***Set operations (union,intersection,difference,symmetric difference)***
#Method:1-> union() and | ->Returns a new set with all elements from both sets
s1={1,2,3,4,5,6,7,8,9}
s2={5,6,7,8,9,10,11,12}
print(s1 | s2) #option: 01
print(s1.union(s2)) #option: 02
#Method:2-> intersection() or &->Returns a new set with elements common to both sets
s1={1,2,3,4,5,6,7,8,9}
s2={5,6,7,8,9,10,11,12}
print(s1 & s2) #option: 01
print(s1.intersection(s2)) #option: 02
#Method:3-> difference() or - ->Returns a new set with elements in s1 but not in s2
s1={1,2,3,4,5,6,7,8,9}
s2={5,6,7,8,9,10,11,12}
print(s1-s2)
print(s1.difference(s2))
#Method:4-> symmetric_difference() or ^ -> Returns a new set with elements in either s1 or s2 but not both
s1={1,2,3,4,5,6,7,8,9}
s2={5,6,7,8,9,10,11,12}
print(s1^s2)
print(s1.symmetric_difference(s2))

#***Checking subsets and supersets***
#Method:1->issubset()->True if all elements of another set are present in this
a={1,2}
b={1,2,3,4}
print(a.issubset(b))
#Method:2->issuperset()->True if all elements of another set are present in this
a={1,2}
b={1,2,3,4}
print(b.issuperset(a))

#***Looping through sets***
my_set={1,2,3,4}
for i in my_set:
    print(i)

#***Set Comprehension***
squared_numbers={x:x**2 for x in range(5)}
print(squared_numbers)


#***Frozenset***
#Frozenset is an immutable set object, meaning it cannot be changed after creation
my_frozenset=frozenset([1,2,3,4,5])
my_frozenset.remove(6)
print(my_frozenset)