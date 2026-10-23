# %%
#if-elif-else statements
import requests

response = requests.get("https://api.github.com")

print(response.status_code)

if response.status_code == 200:
    print("Fuck OpenAI")
# %%
#our first python program
"""
This is a simple Python program that greets the user and asks for their name and age.
this is muitline comment
"""
#write the code - and comment "why" this code is written not write -  what is it code 
name = input("Enter your name: ")
print(f"Hello, {name}!")
age_1 = int(input("Enter your age: "))
if age_1 >= 18 and age_1 <= 100:
    print("You are an adult.")
elif age_1 > 100:
    print("You are dead")
elif age_1 < 18:
    print("You are a minor.")
else:
    print("you are not a human")
# %%

age_2 = int(input("Enter your age: "))
has_license = True

if age_2 >= 18 and has_license:
    print("You can drive.")
elif age_2 >= 18 and not has_license:
    print("You need a license to drive.")
else:
    print("You are too young to drive.")    

# %%
# Loops
for i in range(5):
    print(f"This is loop iteration {i}")
for i in range(1, 11):
    print(f"This is loop second iteration {i}")

for i in range(0, 10, 2):
    print(f"This is loop third iteration {i}" " " "and" " " f"{i}" " " "is a even number")
# %%
for i in range(1, 11):
    print("hello");

# %%
#data structures
#!!!!importaNT lists uses [], dictionaries uses {}, sets uses {} and tuples uses ()
#lists
my_list = [1, 2, 3, 4, 5]
my_list.append("mithu is a good boy");

print("the appended element is" , my_list[5]);
# %%

#dictionaries
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("the city is" , my_dict["city"]);
# %%
#sets
my_set = {1, 2, 3, 4, 5}    
print("the set is" , my_set); 
# %%
#tuples
my_tuple = (1, 2, 3, 4, 5)
print("the tuple is" , my_tuple);
# %%
#functions
lists_1=[1, 2, 3, 4, 5]
print("the length of the list is" , len(lists_1));
#here print and len are built-in functions in python and we can use them without defining them
# %%
#defining our own function
def greets():
    print("hello")
    print("how are you")
    pass    

greets()

# %%
def send_email():
    emailIsSent = True
    if emailIsSent == True:
        print("email sent")
    else:
        print("email not sent")
send_email()
# emailIsSent=bool(int(input("Enter email status (1 for sent, 0 for not sent): ")))
# %%
#parameters and arguments
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.
#if we have 2 parameters in functions parentheses then we have to pass 2 arguments in function call otherwise it will give error

def greet_user(name): # name uused as parameter
    print(f"Hello, {name}!")
greet_user("mithu") # mithu is used as an argument
# %%
 
def add_numbers(num1, num2, num3): # num1, num2, num3 are parameters
    print(num1 + num2 + num3)

add_numbers(5, 10, 12) # 5 and 10 are arguments

# %%
#we can have default parameters in functions, without argumments the default parameters will be printed

def greet_user(name="User"): # default  
    print(f"Hello, {name}!")

greet_user() 
greet_user("Alice") 

# %%
#fun tax calculator
discount = 10
def calculate_total(price, tax_rate=0.1, discount=12):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"actual price: ${price}")
    print(f"Total: ${final_price}")
    print(f"tax: ${tax}", "and " f"discount: ${discount}")

calculate_total(145)
print(f"the global var discount is: {discount}")
 
# %%
#global and local variables
print(f"python which are written outside of the functions are called global functions")
# %%
# returning values from functions
def add_print(a,b):
    return a+b

result = add_print(a=45, b=45)
print(f"the return value is {result+1}")
# %%
def calculator(num1, num2, method = str):
    if method == "add":
        add = num1 + num2
        print(f"the addition is: {add}")
    elif method == "minus":
        minus = num1 - num2
        print(f"the minus  is: {minus}")
    elif method == "mul":
        mul = num1*num2
        print(f"the Mul is: {mul}")
    elif method == "all":
        add = num1 + num2
        minus = num1 - num2
        mul = num1* num2
        print(f"the addition is: {add}")
        print(f"the minus  is: {minus}")
        print(f"the Mul is: {mul}")
    
calculator(
    method=input("Enter which one you want to do (add, minus, mul, all): "),
    num1=int(input("Enter num1: ")),
    num2=int(input("Enter num2: ")),
)
# %%
#external tools
# 'packages' are two types "built-in" and 'external' 
# built-in needs no installation, external need to be installed by pip
#'module' is a single file
#a 'folder' containing multiple modules
#a 'class' is like a blueprint for building objects
# module - toobox, package - garage, functions - a specific tool(hammer, screw driver), class - blueprint for building tools

# %%
import math 
from math import pi
radius = 12
area_of_circle = radius * radius * pi 
print(f"the area of circle is: {area_of_circle}")
# %%
import random

number = random.randint(1,10)
print(number)
# %%
from datetime import datetime

now = datetime.now()
print(now)

# %%
from mypackage.greetings import say_hello
I = input("Enter your name: ")
print(say_hello(I))

# %%
import requests
import json

latitude = 40.7128
longitude = -74.0060

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response1 = requests.get(url)
data = response1.json()

print(json.dumps(data["current_weather"], indent=4))
# %%
