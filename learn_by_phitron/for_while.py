##for - for each item in this collection, do something
## while - keep doing this as long as this condiotion is true
#1. for: work through a collection
# %%
questions = [
    "What internet sales by year?", 
    "What is the total revenue for each quarter?",
    "What is the average order value for each product category?"
]

for question in questions:
    print(question)
# %%
for number, question in enumerate(questions, start=1):
    print(f"Question {number}: {question}")
# %%
for attempt in range (1, 10): 
    print(f"MDX attempt {attempt}")
# %% 
execution_results = bool(input("Enter yes or false:"))

attempt = 0 
success = False 

while attempt < 4 and not success: 
    success = execution_results[attempt]
    attempt += 1 
    print(f"Attempt {attempt}: success = {success}")

print(f"Finish after {attempt} attempt(s)")

# %%
#2. while: repeat until a condition changes
attempts_1 = 0
while attempts_1 < 3:
    execution_results_1 = int(input("Enter yes or no (1 or 0):"))
    attempts_1 += 1

    if execution_results_1 == 1:
        print("Congrats!!!")
        break

    elif execution_results_1 == 0:
        if attempts_1 == 3:
            print("You are out of your attemps")
        else:
            print("Try again")
# %%
#Write a program that uses:
#- A for loop to go through the three questions.
#- A while loop to give each question at most two attempts.
#- input() to ask whether the generated MDX worked: 1 for success, 0 for failure.
#Rules:
#1. Print the question before testing it.
#2. If the user enters 1, print "Passed" and move to the next question immediately.
#3. If the user enters 0 on the first attempt, print "Try again".
#4. If both attempts are 0, print "Failed: out of attempts".
#5. After all questions, print how many passed and how many failed.
#For example, if the inputs are 0, 1 for question 1; 1 for question 2; and 0, 0 for question 3, the final result should be 2 passed, 1 failed.
#Tricky part: break should end the attempts for the current question, but the for loop must continue to the next question. Try writing it yourself and send me your code.

questions_2 = [
    "What internet sales by year?",
    "What is the total revenue for each quarter?",
    "What is the average order value for each product category?"
]

while True:
    passed = 0
    failed = 0

    for question in questions_2:
        print(question)
        attempts = 0
        success = False

        while attempts < 2 and not success:
            execution_result = int(input("Enter yes or no (1 for success, 0 for failure): "))
            attempts += 1

            if execution_result == 1:
                print("Passed")
                passed += 1
                success = True
                break
            elif execution_result == 0:
                if attempts == 2:
                    print("Failed: out of attempts")
                    failed += 1
                else:
                    print("Try again")

    print(f"Final Result: {passed} passed, {failed} failed.")
    break
# %%







