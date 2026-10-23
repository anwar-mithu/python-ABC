#we will learn about functions in python
#run the code in a loop until the user enters a valid score between 0 and 100
# %%   
for i in range(3):
    score = int(input("Enter your score:"))
    if score >= 0 and score <= 100:
        print(f"Valid score entered: {score}")
        break
    else:
        print("Invalid score. Please enter a score between 0 and 100.")

# %%
#what is function in python?
#function is a block of code that performs a specific task and can be reused multiple times in a program. Functions help to organize code, make it more readable, and reduce redundancy. In Python, functions are defined using the `def` keyword, followed by the function name and parentheses.

def greet(name):
    return f"Fuck you, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
# %%
def build_mdx(measure, time_level):
    query = (
     f"SELECT {{ [Measures].[{measure}] }} ON COLUMNS, "
        f"[Date].[{time_level}].Members ON ROWS "
        f"FROM [Adventure Works Internet Sales Model]"    )
    return query

mdx = build_mdx("Internet Sales Amount", "Calendar Quarter")
print(mdx)
# %%

