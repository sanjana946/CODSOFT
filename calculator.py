# Get the two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display the operation choices
print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform the calculation based on the user's choice
if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == '4':
    if num2 == 0:
        print("\nError! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid input! Please choose a number from 1 to 4.")
