def calculator(a, b, operation):
    """
    Perform a calculation based on the given operation.

    Parameters:
    a (float): The first number.
    b (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the calculation.

    Raises:
    ValueError: If an invalid operation is provided or if division by zero is attempted.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Invalid operation '{operation}'. Supported operations are: add, subtract, multiply, divide.")