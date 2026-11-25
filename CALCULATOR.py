
def calculator():
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-7): ")

            if choice == '7':
                print("Thank you for using the calculator!")
                break

            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid choice. Try again.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            elif choice == '5':
                if num2 == 0:
                    print("Error: Modulus by zero!")
                    continue
                result = num1 % num2
            elif choice == '6':
                result = num1 ** num2

            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        except OverflowError:
            print("Error: Result is too large.")


if __name__ == "__main__":
    calculator()
