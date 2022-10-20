from art import logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(f"{logo}")
    # First number input
    num1 = float(input("What's the first number?: "))
    # Display operators to use
    for symbol in operations:
        print(f"{symbol}")
        
    # Ask user if they wish to continue calculations
    should_continue = True

    while should_continue:
        # Select operator
        operation_symbol = input("Pick an operatior: ")
        # Second number input
        num2 = float(input("What's the next number?: "))
        # Select the correct dictionary operation
        calculation_function = operations[operation_symbol]
        # Calculate the answer
        answer = calculation_function(num1, num2)
        # Print the equation and answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y to continue calculating with {answer}, or type 'n' to start a new calculation.") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()