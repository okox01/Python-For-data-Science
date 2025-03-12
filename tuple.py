#***Creating tuple***
#Method:1-> with multiple elements
tuple1=(1,2,3,4,5)
print(tuple1)
#Method:2-> with single element
tuple2=(1) # indicates integer value
print(type(tuple2))
tuple3=(2,) # indicates tuple value
print(type(tuple3))
print(tuple3)

#***Tuple Nesting***
nested_tuple=(1,(2,3),["sami",True],(3.4,(45,"sayed")))
print(nested_tuple)
print(nested_tuple[3][1][1])


#***Sorting Tuple***
Ratings=(0,9,6,5,10,8,9,6,2)
sorts=sorted(Ratings)
print(type(tuple(sorts)))
print(sorts)

#***tuple operations***
tuple1=(1,2,3,4,5)
tuple2=(4,5) #tuple allows duplicate values
print(tuple1+tuple2) #concatenation
print(tuple1*3) #repetition

# sum()->adds all the numbers in the tuple
s=sum(tuple1)
print(s)

#max()->finds the maximum from the tuple
m=max(tuple1)
print(m)

#min()->finds the minimum from the tuple
mi=min(tuple1)
print(mi)

#Counter()-> find the occurences of the same number or characters
from collections import Counter
t=(1,1,5,4,1,5,5,4,1)
c=Counter(t)
print(c)

#***Enumerate()->used for getting value and index at the same time using for loop
tuple2=("sami",1,("hello","world"))
for index,value in enumerate(tuple2):
    print(f"index {index}:{value}")

#***tuple slicing***
tuple1=(1,2,3,4,5,6,7,8,9)
print(tuple1[0:7:2])

#***tuple length***
tuple1=(1,2,3,4,5,6,7,8,9)
print(len(tuple1))


