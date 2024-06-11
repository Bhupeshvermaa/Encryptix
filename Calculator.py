def calculator():
    """Performs basic arithmetic operations based on user input."""

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero not allowed")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")

            print("Result:", result)
            break  # Exit loop after successful calculation

        except ValueError:
            print("Invalid input. Please enter numbers and a valid operator (+, -, *, /).")
        except ZeroDivisionError as e:
            print(e)  # Print the ZeroDivisionError message

if __name__ == "__main__":
    calculator()
