
#finally
raw = input("Enter a number: ")

try:
    check_input = int(raw)
except ValueError:
    try:
        check_input = float(raw)
    except ValueError:
        print("this is not a number. Please enter a valid number.")
    else:
        print("this is a float number. We will not store it in the database.")
else:
    if check_input < 0:
        print("But the number is negative. We will not store it in the database.")
    elif check_input > 100:
        print("But the number is greater than 100. We will not store it in the database.")
    else:
        print("The number is valid, between 0 and 100. So, it will be stored in the database.")
finally:
    print("Execution completed.")     

