# %%
num = float(input("Enter a number: "))
print(type(num))
# %%
for i in range(5, 0, -1): # what is it mean? 5 to 0, decrement by 1
    if i % 2 == 0: # what is it mean? if i is even
        continue # what is it mean? skip the rest of the loop and go to the next iteration
    if i == 3: # what is it mean? if i is 3, then break the loop
        break
    print(i, end=" ") # what is it mean? print i in the same line 
# %%
x = [1, 2, 3, 2, 4]
x.remove(4) # what is it mean? remove the first occurrence of 4 from the list
x.pop() # what is it mean? remove the last element from the list
print(x)
# %%
{'a': 1, 'b': 2}.keys() # what is it mean? return the keys of the dictionary
#9. Which method is used to remove an item from a dictionary by key?
#answer: del dict[key] or dict.pop(key)
print(7//2)


# %%
#Which of the Which of the following has the highest precedence in Python?
#anwer: and? or? not? not has the highest precedence in Python
# it means that not is evaluated first, then and, then or