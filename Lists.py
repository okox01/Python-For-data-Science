#***Creating List***
#Method:1-> simple List 
list1=[1,2,3,4]
print(list1)
#Method:2-> Mixed list
mixed_list=[1,"Python",True,3.14]
print(mixed_list)
#Method:3-> Nested List
nested_list=[1,2,[3,4,5],(5,9,"sami")]
print(nested_list)

#***Accessing elements***
#Method:1-> by index
p=[1,2,[3,4,5],(5,9,"sami")]
print(p[3][2])

#***Modifying List***
#Method:1-> direct modification
p=[1,2,[3,4,5],(5,9,"sami")]
p[3]="ok"
print(p)

#***Extend Method***
#Method:1-> extend with another list
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
#Method:2-> extend with a tuple
list1=[1,2,3]
tuple1=(4,5,8)
list1.extend(tuple1)
print(list1)
#Method:3-> extend with a string
list1=[1,2,3]
list1.extend("cd")
print(list1)
#Method:4-> extend a list with a set
list1=[1,2,3]
set1={4,5}   #the order of set element is not guarenteed
list1.extend(set1)
print(list1)

#***Append Method***
list1=[1,2,3,4,5]
list1.append(8)
print(list1)

#***Difference between extend and append***
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2) #extend method add all elements of list2 to list1
print(list1)
list1=[1,2,3]
list2=[4,5,6]
list1.append(list2) #append a list all in one index
print(list1)

#***List Operations***
list1=[5,2,3]
list2=[10,5,6]
print(list1+list2) #List Concatenation
print(list1*4) #List Repetition

#***List Methods***
#Method:1-> sort()
list1=[10,8,2,4,7]
list1.sort() #sort list in ascending order
print(list1)
#Method:2-> reverse()
list5=[4,7,1,10]
list5.reverse()
print(list5)
#Method:3-> remove()
list1=[1,2,3,4,5]
list1.remove(2)
print(list1)
#Method:4-> pop()
list1=[1,2,3,4,5]
list1.pop(2) #pop the element at index 2
print(list1) 
list1.pop()
print(list1)#pop the last element


#***List Slicing***
    #l[start:end:jump]
    #start:from which index to start
    #end:from which index to end
    #jump:how many steps to jump
list1=[10,20,("sami",False),[3.14,(False,145)]]
print(list1[0:4:2]) #[10, ('sami', False)]

#***delete an element from list***
#Method:1-> using del
list1=[1,2,3,4,5]
del(list1[0])
print(list1)
#Method:2-> using pop()
list3=[1,8,9,7,3]
list3.pop() #pop the last element
list3.pop(2) #pop the element at index 2
print(list3)
#Method:3-> using remove()
list1.remove(2)
print(list1)

#***Copy and Clone Lists***
#Method:1-> copy()
list2=[4,5,6,77]
list3=list2.copy()
print(list3)
#Method:2-> Clone
l1=[4,5,6,9]
l2=l1 #referencing to the same list
l1[0]="sami"
print(l1)
print(l2)

l3=[5,8,9,10]
l4=l3[:] # referencing to the different addresses
l3[0]="sayed"
print(l3)
print(l4)

#***split()***
a="sami".split()
print(a)
b="a,b,c,d,e".split(',') #split by comma [delimeter]
print(b)


