#we will learn about if, elif and else statements in python
#run the code in a loop until the user enters a valid score between 0 and 100
## %%
while True:
    score = int(input("Enter your score:"))
    if score >= 0 and score <= 100:
        break
    else:
        print("Invalid score. Please enter a score between 0 and 100.")

if score > 100:
    print ("unvalid score!")
elif score >= 90 and score <= 100:
    print ("Excellent!")
elif score >= 80:
    print ("Good job!")
else:
    print ("Keep trying!")  

# %%
while True:
    attemps = int(input("How many attempts did it take to execute the model? (Enter a number): "))
    if attemps > 3:
        print("Too many attempts! Please try again later.")
        break
    execution_success = input("Was the model executed successfully? (yes/no): ").lower()
    
    if execution_success == "yes":
        print("Great! The model executed successfully.")
    elif execution_success == "no":
        print("Please check the model and try again.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    break
