#***Creating Dictionary***
#Method-1-> using {}
my_dict={"name":"sami","age":23,"gender":"male"}
print(my_dict)
#Method-2-> using dict()
my_dict2=dict(name="sayed",age=25,subject="Math")
print(my_dict2)
#Method-3-> empty dictionary
my_dict3={}
print(type(my_dict3)) #<class 'dict'>

#***Accessing values in Dictionary***
#Method-1-> using key
print(my_dict["name"])
#Method-2-> using get()
print(my_dict.get("age"))
print(my_dict.get("height","Not found"))

#***Adding and Updating Dictionary elements***
#Method-1-> update existing key
my_dict["name"]="sayed"
print(my_dict)
#new key-value pair
my_dict["country"]="AUSTRALIA"
print(my_dict)

#***Removing elements from a dictionary***
#Method-1-> using pop()->Removes key and returns its value
age=my_dict.pop("age")
print(age)
#Method-2-> using del
del my_dict["gender"]
print(my_dict)
#Method-3-> using popitem()->removes last inserted item
last_item=my_dict.popitem()
print(last_item)
#Method-4-> using clear()->removes all items
my_dict.clear()
print(my_dict)


#***Dictionary Methods or operations***
student={"name":"sami","id":945,"Dep":"CSE","Cgpa":3.88}
#Method-1: keys()
print(student.keys())
#Method-2: values()
print(student.values())
#Method-3: items()
print(student.items())

#***Looping through a dictionary***
#Method-1: by key
for key in student:
    print(key,end=" ") #end doest allow the output to show in a new line
#Method-2: by value
print("\n")
for value in student.values():
    print(value,end=" ")
#Method-3: by key-value pair
print("\n")
for key,value in student.items():
    print(f"{key}:{value}")

#***Dictionary Comprehension***
#concise way to create dictionary
squares={x:x**2 for x in range(5)}
print(squares)

#***Nested Dictionary***
#Dictionary can conatain another dictionary
Students={
        "Alice":{"age":25,"major":"Physics"},
        "Bob":{"age":23,"major":"Math"}
    }
print(Students["Alice"]["major"]) #accessing nested dictionary

#***Dictionary Merging***
#combining two dictionaries
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged=dict1|dict2
print(merged)

#***Sorting Dictionary***
person={"z":3,"a":1,'c':2}
sorted_dict=dict(sorted(person.items()))
print(sorted_dict)

#***Default Dictionary(from collections)
#A default dictionary allows setting a default value type
from collections import defaultdict
dd=defaultdict(int)
dd['x']+=1 #no keyerror, initializes with default valeu int(0)
print(dd)

#***Counter(for counting elements)***
from collections import Counter
#counting elements in a list
text=Counter("hello world")
print(text)



