# loop in python
# range(x,y,z) , here x is the starting point, y is the ending point, and z is the step value.
value_increase = []
for i in range(5,101,5):
    value_increase.append(i)

print(value_increase)

value_decrease = []
for i in range(100,0,-5):
    value_decrease.append(i)
print(value_decrease)
# print hello world 20 times with the increasing value of i, step 5
value_hello_world = []
for i in range(5,101,5):
    value_hello_world.append(i)
    print(f"{i}: Hello World")

# lets learn while loop in python
# %%
x = int(input("Enter a number: "))
while x <100:
    print("Fuck you!!!!")
    x += 1
# %%
# continue and break in python
sum = 0
for i in range(1, 11):
    # add only even numbers from 1 to 10 and their sum
    if i % 2 != 0:
        continue
    sum += i
    print(i, sum)

# %%
for i in range(1, 11): 
    if i % 2 == 0:
        continue # here continue means skip the even numbers of the loop and go to the next iteration
    sum += i
    print(i, sum)
# %%
# add odd number with while loop
i = 1
sum = 0
while i < 11:
    if i % 2 == 0:
        i += 1
        continue
    sum += i
    print(i, sum)
    i += 1
# %%
# lets use break in for loop
accuracy = 70.00
for i in range(101):
    accuracy += 1
    if accuracy == 100.00:
        break
    print(f"Accuracy: {accuracy}%")

# %%
accuracy_1 = 70.00
while True:
    if accuracy_1 == 100.00:
        break
    accuracy_1 += 1
    print(f"Accuracy: {accuracy_1}%")

# %%
# min and max in python
x = [1, 2, 3, 4, 5]
print(min(x)) # what is it mean? return the minimum value from the list
print(max(x)) # what is it mean? return the maximum value from the list

# %%
import random
random_number = random.randint(1, 100) # what is it mean? return a random integer between 1 and 100
print(random_number)
x = int(random_number)
print(x)
#print(min(random_number), max(random_number))
# %%

numbers = [-5, 0, -3, -10, 12, 5, 7]

count_negative = 0
count_positive = 0
count_zero = 0
count_even = 0
count_odd = 0

for i in range(len(numbers)):
    if numbers[i] < 0:
        count_negative += 1
        print(f"{numbers[i]} is negative")
    elif numbers[i] > 0:
        count_positive += 1
        print(f"{numbers[i]} is positive")
    elif numbers[i] == 0:
        count_zero += 1
        print(f"{numbers[i]} is zero")
    elif numbers[i] % 2 == 0:
        count_even += 1
        print(f"{numbers[i]} is even")
    else:
        count_odd += 1
        print(f"{numbers[i]} is odd")

print(f"Total negative numbers: {count_negative}")
print(f"Total positive numbers: {count_positive}")
print(f"Total zero numbers: {count_zero}")
print(f"Total even numbers: {count_even}")
print(f"Total odd numbers: {count_odd}")
    

# %%

space_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print reverse of the list
# print 4 spaces between each number
space_numbers.reverse()
for i in space_numbers:
    print(i, end="     ")


# %%

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# %%
for i in range(10):
    if i > 5:
        break
    print(i)
else:
    print("Loop finished without breaking")
# %%
x = 5
while x > 0:
    x -= 1
    if x == 2:
        break
    print(x)

# %%
