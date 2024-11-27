#!/usr/bin/env python3

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unsupported operation"


# Main program
def main():
    try:
        # Get user input
        user_input = input("Enter two numbers and an operation separated by spaces (e.g., 10 5 +): ")
        parts = user_input.split()

        # Validate input
        if len(parts) != 3:
            print("Error: Please enter two numbers and an operation (e.g., 10 5 +).")
            return

        num1 = float(parts[0])  # Convert first number to float
        num2 = float(parts[1])  # Convert second number to float
        operation = parts[2]  # Get operation as string

        # Perform calculation
        result = calculate(num1, num2, operation)

        # Print the result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Error: Invalid number entered.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()




