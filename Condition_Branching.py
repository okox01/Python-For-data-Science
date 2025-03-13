# #***if elif and else statements***
age =int(input("whats your age: ")) #taking input from user which is an integer number
if age<18 and age>=0:
    print("you are not adult")
elif age>=18 and age<=30:
    print("you are young adult")
elif age>30 and age<=60:
    print("you are adult")
elif age>60 and age<140:
    print("you are so old")
else:
    print("invalid age")

#***Nested if***
age=20
if age>=18:
    if age>=21:
        print("you are mature")
    else:
        print("you are an adult but not mature")

#***Logical operators in conditions***
# ***and***
age=20
has_license=True
if age>=18 and has_license:
    print("you can drive")
else:
    print("you can not drive")

#***or***
is_raining=False
sunny_day=True
if is_raining or sunny_day:
    print("take umbrella")
else:
    print("no need to take umbrella")

#***not***
is_student=False
if not is_student:
    print("you are not a student")
else:
    print("you are a student")


#***ternary operator(short if-else)***
# case-01
age=15
print("you are an adult") if age>=18 else print("you are not an adult")

# case-02
grade="A"
status="good student" if grade=="A" else "bad student"
print(status)

#***using condition in loops***
#for loop
number=[1,2,3,4,5]
for n in number:
    if n%2==0:
        print(n)

#while loop
i=0;
while i<=5:
    if i%2==0:
        print(i)
    i+=1

#***pass , break and continue***
#pass
x=10
if x>5:
    pass # do nothing and move to the next line can be implemented later

#break statement
for i in range(10):
    if i==5:
        break
    print(i)

#continue statement
for i in range(5):
    if i==2:
        continue
    print(i)

#***Match-Case***
#code:
grade="B"
match grade:
    case "A":
        print("Exellent")
    case "B":
        print("Good")
    case "C":
        print("Needs improvement")
    case _:
        print("Invalid grade")


#***is vs == conditions***
a=[1,2,3]
b=[1,2,3]
print(a==b) #True: same value
print(a is b) #False: different memory locations

