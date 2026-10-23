# %%
#class object, __init__
class fruits: 
     def __init__(self, name, color, shape): # here __init__ is a constructor, it is used to initialize the attributes of the class. other things like here, name, color, shape are attributes of the class.
         self.name = name
         self.color = color
         self.shape = shape

fruits_object_1 = fruits("Apple", "Red", "Round") # fruits_object_1 is an object of the class fruits. It is created by calling the constructor of the class fruits and passing the values for the attributes name, color, and shape.
fruits_object_2 = fruits("Banana", "Yellow", "Curved")
fruits_object_3 = fruits("Orange", "Orange", "Round")

print(fruits_object_1.name)
print(fruits_object_1.color)
print(fruits_object_1.shape)

print(fruits_object_2.name)
print(fruits_object_2.color)
print(fruits_object_2.shape)

print(fruits_object_3.name)
print(fruits_object_3.color)
print(fruits_object_3.shape)

# %%
class MDXRun: 
    x = 5
p1 = MDXRun()
print(p1.x)
# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emily", 36)
print(f"Her name is {p1.name} and Her age is: {p1.age}")

# %%

# %%
