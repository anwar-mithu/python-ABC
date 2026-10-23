#get execution result from user
#we will need to get three questions result from the user
result_question_1 = {
    1: "",
    2: "",
    3: ""
}

for result in range(3):
    executed = int(input(f"for question {result + 1} : Enter 1 if the query executed successfully, or 0 if it failed: "))
    semantically_correct = int(input(f"for question {result + 1} : Enter 1 if the query is semantically correct, or 0 if it is semantically incorrect: "))

    def evaluate_query_1(executed, semantically_correct):
        if executed == 1 and semantically_correct ==  1:
            return f"Query for question {result + 1} did execute and is semantically correct."
        elif executed == 1 and semantically_correct == 0:
            return f"Query for question {result + 1} did execute but is semantically incorrect."
        else:
            return f"Query for question {result + 1} did not execute."

    result_question_1[result + 1] = evaluate_query_1(executed, semantically_correct)
 
print(result_question_1)


# %%
#i have 4 MDX question for each questions the user give me two inputs. did mdx executed or not and does it have rows or not

result_question_2 = {
    1: "",
    2: "",
    3: "",
    4: ""
}

for question in range(4): 
    executed = int(input(f"for question {question + 1} : Enter 1 if the query executed successfully, or 0 if it failed: "))
    has_rows = int(input(f"for question {question + 1} : Enter 1 if the query has rows, or 0 if it does not have rows: "))

    def evaluate_query_2(question_num, executed, has_rows):
        if executed == 1 and has_rows == 1:
            return f"Query for question {question_num} did execute and has rows."
        elif executed == 1 and has_rows == 0:
            return f"Query for question {question_num} did execute but does not have rows."
        else:
            return f"Query for question {question_num} did not execute."

    result_question_2[question + 1] = evaluate_query_2(question + 1, executed, has_rows)

print(result_question_2)