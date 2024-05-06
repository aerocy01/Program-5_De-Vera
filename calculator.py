def calculate(operation, num1, num2):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Please choose from Addition, Subtraction, Multiplication, or Division.")

def main():
    while True:
        try:
            operation = input("Choose one of the four math operations (Addition, Subtraction, Multiplication, Division): ").capitalize()
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calculate(operation, num1, num2)
            print(f"The result is: {result}")
            continue_program = input("Do you want to try again? (yes/no): ").lower()
            if continue_program != 'yes':
                print("Thank you!")
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()