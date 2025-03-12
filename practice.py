person={"name":"sami","age":23,"gender":"Male"}
person2=dict(name="sayed",age=25,gender="Female")
person3={}

print(person["name"])
a=person.get("age")
print(a)

print(person.get("country","error"))

person["name"]="alex"
print(person)

person["country"]="USA"
print(person)

a=person.pop("name")
print(a)

del person["country"]
print(person)

print(person2.popitem())

person.clear()
print(person)

person3={"name":"Alice","age":25,"gender":"Female","Country":"Italy"}
print(person3.keys())

print(person3.values())
print(person3.items())

for i in person3:
    print(i,end=" ")
print("\n")
for j in person3.values():
    print(j,end=",")
print("\n")
for i,j in person3.items():
    print(f"{i}:{j}")

squares={x:x**2 for x in range(5)}
print(squares)

student={
        "sami":{"id":945,"cgpa":3.88},
        "Artho":{"id":932,"cgpa":3.95},
        "saimon":{"id":936,"cgpa":3.9}
    }
print(student["sami"]["id"])


dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged=dict1 | dict2
print(merged)

dict5={"A":5,"C":2,"D":1,"B":3,"E":4}
sorted_dict=dict(sorted(dict5.items()))
print(sorted_dict)

from collections import defaultdict
dd=defaultdict(int)
dd["a"]=1
print(dd)

from collections import Counter
text=Counter("iam sami")
print(text)

list1=[1,2,4,5]
list1.extend(["sami"])
print(list1)

list3=[1,1,3,4,4,5,5]
print(list3)

my_dict={"name":"sami","age":23,"gender":"male"}
age=my_dict.pop("name")
print(age)