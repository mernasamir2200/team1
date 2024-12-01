def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

    # Deliberate error: using "==" instead of "in" for checking multiple options
    if operation == ['1', '2', '3', '4']:
        # Get user input for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            # Deliberate error: missing '=' in addition
            if operation == '1':
                print(f"The result is: {num1 + num2}")  # This one is fine
            elif operation == '2':
                print(f"The result is: {num1 - num2")
            elif operation == '3':
                print(f"The result is: {num1 * num2}")  # Deliberate mistake: num1 + num2
            elif operation == '4':
                # Deliberate error: dividing without checking for zero
                print(f"The result is: {num1 // num2}")
        except ValueError:
            # Deliberate error: typo in error message
            print("Erro: Invalid input. Please enter numeric values.")
    else:
        # Deliberate error: wrong message for invalid input
        print("Error: Please restart.")
calculator()
