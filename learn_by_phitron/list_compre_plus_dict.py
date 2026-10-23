#difference between list and array is that list can hold different data types while array can only hold same data type.
#difference between dictionary and array is that dictionary holds key value pairs while array holds only values.
#difference between list and dictionary is that list holds values while dictionary holds key value pairs.
# %%
#list comprehension with dictionary
numbers = [1, 2, 3, 4, 5]
squares = [x *x for x in numbers]
print(squares) 
# %%

success_ids = []
failed_ids = []

for i in range(3):
    def get_input():
        return int(input(f"for Q{i + 1}: Enter 1 for True, 0 for False: "))
    
    runs = [
        {"id": f"Q{i + 1}", "executed": get_input()},
    ]
    
    success_ids.extend(run["id"] for run in runs if run["executed"])
    failed_ids.extend(run["id"] for run in runs if not run["executed"])
    
print(f"Successful IDs: {success_ids}")
print(f"Failed IDs: {failed_ids}")
# %%
#array code without using numpy
array = [1, 2, 3, 4, 5]
squared_array = [x**2 for x in array]
print(squared_array)


# %%
#dictionary code 
dict1 = {'a': 1, 'b': 2, 'c': 3}
# Using dictionary comprehension to create a new dictionary with squared values
squared_dict = {k: v**2 for k, v in dict1.items()}  
print(squared_dict)