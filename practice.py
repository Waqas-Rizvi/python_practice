# print("Hello World")
# print("Hello ", end="")
# print("Waqas", "Altaf", sep=", ")

# print("""
# print("A")
# print("B")
# print("C")
# print("A", end="")
# print("B", end="")
# print("C")
# print("A", "B", "C", sep=",")
# """)

# if 5 > 2:
#   print("Five is greater than two!")

# if 5 > 2:
#  print("Five is greater than two!")
# if 5 > 2:
#     print("Five is greater than two!")

"""
x = 5
y = 7 #this is variable
print(x+y)
"""

# print("Math", 50, sep=":")
# print("Math:", 50)

# x = int(8)
# print(x+2)

# x = str(3.0)
# print(type(x))

# Case Sensitive
# x = 1
# X = 2
# print(x)
# print(X)

# print('There are three "Chickens" in the house')

"""
name = "Waqas"
age = 24
city = "Karachi"
print("My name is", name)
print("I'am", age, "years old")
print("I live in", city)
"""

"""
name = "Waqas"
age = 24
city = "Karachi"
dollar_rate = 277
print("My name is", name, "I'am", age, "years old, Dollar rate in Pakistan is", dollar_rate)
print(f"My name is {name}, I'am {age} years old, Dollar rate in Pakistan is {dollar_rate}")
"""

# x = str(2)
# y = 3
# z = y
# print(type(x))

# x, y, z = str(1), 2, 3
# print(y+z+int(x))

# a = "Waqas"
# x = y = z = a
# print(x+y+z)

# x = 2
# y = str(1)
# print(x, y)

# x = 'altaf'


# def myFunc():
#     global x
#     x = "waqas"
#     print(x)


# myFunc()
# print(x)


# x = complex(1j)
# print(type(x))

# x = 35e3
# print(complex(x))

# import random
# print(random.randrange(1, 9))

# x = 2
# y = "w"
# print(x,y)

# x = """
# My name is Waqas.
# """
# y = '''
# My name is Waqas.
# '''
# print(y)

# string interpolation / f string => f

# name = "Waqas"
# age = 24
# print(f"My name is {name} and my age is {age}")
# print("My name is {} and my age is {}".format(name, age))
# print("My name is %s and my age is %s" % (name, age))

# x = "Hello"
# print(x[4])

# for x in "hello":
#     print(x)

# for y in "waqas":
#     print(y)

# x = "Waqas is Developer"
# # # print(len(x))
# # print("is" in x)
# # print("iss" in x)
# if "iss" in x:
#     print("Yes its present")
# else:
#     print("Its not present")
# if "iss" not in x:
#     print("Its not present")
# else:
#     print("Yes its present")

# scape character = \n => yeh line break krta h or yeh back slash se ata h na k forward slash k
# print("Waqas" + '\n' + "Altaf")
# tab spacing k liay = \t
# print("Waqas" + '\t' + "Altaf")
# \ => yeh apny baad waly ko string consider krleta h
# print('I\'m 30')

# input function
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"My name is {name} and my age is {age}")
# print(type(age))

# x = "Waqas"
# print(x[2:5])

# input("Enter your name: \n")

# x = input("Enter your name: \n")
# print(f"Hi {x.upper()}! Welcome back.")

# x = int(input("Enter first number: \n"))
# y = int(input("Enter second number: \n"))
# print(x+y)

# x = 'waqas'
# print(x.replace("w","a"))
# print(x.split("q"))

# x = input("Enter a number: \n")
# print(f"The square of a number is: {int(x)*int(x)}")

# name = "Waqas"
# age = 24
# print("My name is {1} and my age is {0}".format(name, age))

# math = int(input("Enter marks of Math \n"))
# english = int(input("Enter marks of English \n"))
# physics = int(input("Enter marks of Physics \n"))
# percentage = (math + english + physics)/300*100
# allmarks = f"""
# Math: {math}
# English: {english}
# Physics: {physics}
# Sum: {math + english + physics}
# Percentage: {round(percentage,2)}%
# Multiplication: {math * english * physics}
# Division: {math / english / physics}
# Subtraction: {math - english - physics}
# """
# print(allmarks)

# x = 2
# y = 3
# z = 0
# print("x is ", x)
# print("y is ", y)

# x = "waqas"
# print(isinstance(x, str))
# print(isinstance(x, int))

# x = 13
# print(x % 5)

# /
# // => float division
# x = 11
# y = 2
# print(x/y)
# print(type(x/y))
# print(x//y)
# print(type(x//y))

# +=, -=, *=, /=, //= assignment operator
# x = 20
# x += 2
# print(x)

# print(10 > 8)
# print(10 < 8)

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# comparision operators
# x = 15
# y = 15
# print("x <= y", x <= y)
# print("x >= y", x >= y)

# x = 0
# print(bool(x))

# logical operators => and , or
# a = True
# b = True
# c = False
# d = False
# print(a and b)  # True
# print(a or b)  # True
# print(a or c)  # True
# print(a and d)  # False
# print(a and b or c)  # True
# print(a or b and c)  # True

# def testing():
#     return True


# if testing():
#     print("YES")
# else:
#     print("NO")

# x = 200
# print(isinstance(x, str))

# if and else

# x = 10

# if x > 10:
#     print("Yes")
# else:
#     print("No")

# if x > 10:
#     print("Greater")
# elif x == 10:
#     print("Equal")
# else:
#     print("Less")

# x = "a"
# if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#     print("Its a vowel")
# else:
#     print("Its not a vowel")
# x = -2
# if x >= 0:
#     print("Its Positive")
# else:
#     print("Its Negative")
# x = 10
# if x % 2:
#     print("Its Odd")
# else:
#     print("Its Even")

# value = int(input("Insert your math's Marks: \n"))
# if value >= 80 and value <= 100:
#     print("Grade A+")
# elif value >= 70 and value < 80:
#     print("Grade A")
# elif value >= 60 and value < 70:
#     print("Grade B")
# elif value >= 50 and value < 60:
#     print("Grade C")
# elif value >= 40 and value < 50:
#     print("Grade D")
# elif value >= 0 and value < 40:
#     print("Fail")
# else:
#     print("Please insert a valid number!")

# List

# list = ["Waqas", "Altaf"]
# list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# secondList = ["Papita"]
# list = list(("Waqas", "Altaf", "Waqas"))

# list.clear()
# del list
# list.pop()
# list.pop(2)
# list.remove("apple")
# list.extend(secondList)
# list.append("Papita")
# list.insert(1, "Papita")
# list[1] = "Mango"
# list[1:5] = ["Papita"]
# list[1:2] = ["Mango", "Papita"]
# print(list)
# if "banana" in list:
#     print("Yes Exist")
# else:
#     print("No Exist")
# print(list[-3:-1])
# print(list[3:])
# print(list[:4])
# print(list[4:6])
# print(list[-1])
# print(len(list))
# print(type(list))

# Dictionary | dict

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "colors": ["red", "white", "blue"]
# }
# secondDict = dict(name="John", age=36, country="Norway")

# print(secondDict)
# print(thisdict["model"])
# print(len(thisdict))
# print(type(thisdict))
# print(thisdict["colors"][2])
# print(thisdict.get("colors")[2])
# print(thisdict.keys())
# print(thisdict.values())
# thisdict["Detail"] = "Testing"
# thisdict["colors"] = ["White"]
# print(thisdict.items())
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# thisdict.update({"year": 2020})
# thisdict.update({"detail": 2020})
# print(thisdict | secondDict)
# thisdict.pop("model")
# thisdict.popitem()
# del thisdict["colors"]
# print(thisdict["colors"])
# print(thisdict.get("colors", 0))
# del thisdict
# thisdict.clear()
# for x in thisdict:
#   print(x)
# for x in thisdict:
#   print(thisdict[x])
# for x, y in thisdict.items():
#   print(x, y)
# x = thisdict
# x = thisdict.copy()
# x = dict(thisdict)
# print(x)

# dict = {
#     "name": "Waqas",
#     "age": 24,
#     "gender": "male",
# }
# dict2 = {
#     "address": "Bantwa Nagar",
#     "street": 10,
#     "house_no": 302,
# }
# dict.update({"salary": '$500', "department": "Senior developer",
#             "joining_date": '10-August-2023'})
# dict.pop("age")
# dict.update({"dob": "19-Sep-1998"})
# del dict["dob"]
# dict.update({"date_of_birth": "19-Sep-1998"})
# print(dict)
# print(dict | dict2)

# for loop

# contacts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for id in contacts:
#     if id == 3 or id == 4:
#         continue
#     if id == 8:
#         break
#     print("Contacts", id)

# for x in range(2, 6):
#   print(x)

# for x in range(7, 49, 7):
#   print(x)
# else:
#   print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "xyz":
#     print("availabe")
#     break
# else: # yeh us waqt chalta h jub loop complete chal jata h
#     print("not availabe")

# for x in [0, 1, 2]:
#     pass

# x = {
#     "id": 1,
#     "name": "Waqas"
# }
# x = ["Waqas", "Altaf"]
# for key, val in enumerate(x):
#     print(key, val)

# x = [
#     {
#         "id":1,
#         "name":"Waqas"
#     },
#     {
#         "id":2,
#         "name":"Altaf"
#     },
# ]
# for key,val in enumerate(x):
#     if val.get("name") == "Altaf":
#         print(val)

# for i in range(1,5):
#     for j in range(i):
#         print(j)

# while loop

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# x = 5
# while x > 0:
#     print(x)
#     x -= 1

# user_input = input("Enter a number between 1 and 10 \n")
# user_input = int(user_input)

# while user_input < 0 or user_input > 10:
#     user_input = input("Enter a number between 1 and 10 \n")
#     user_input = int(user_input)

# print("Valid number is", user_input)

# x = 1
# while x <= 20:
#     print(x)
#     x += 1

# index = 0
x = [1, 2, 3, 4, 5]

# while index < 5:
#     if len(x) != 0:
#         x.pop()
#     print(x)
#     index += 1

# print(x)
# while len(x) > 0:
#     x.pop()
#     print(x)

# print("Empty Array!")

# Functions

# def my_function(age = 20):
#   print(f"My age is {age}")

# my_function()
# my_function(22)

# def math(x):
#     return x * 2
# print(math(10))

# def empty():
#     pass

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print("first", result, k)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(8)


# def x(a, b=4): return a + b


# print(x(5))

# x = [
#     {
#         "id": 1,
#         "name": "Waqas",
#         "age": 12
#     },
#     {
#         "id": 2,
#         "name": "Saad",
#         "age": 15
#     },
#     {
#         "id": 3,
#         "name": "Hamza",
#         "age": 20
#     },
# ]


# def my_function(id):
#     for i in x:
#         if i.get("id") == id:
#             return i


# z = my_function(3)
# print(z)
