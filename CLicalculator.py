# Simple CLI Calculator Task
# Accepts user input
print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. MODULO")

operation = input()

if operation == "1":
    first_number = input("Enter first number: ")
    second_number = input("Enter Second number: ")
    print("Sum is " + str(int(first_number) + int(second_number)))

elif operation == "2":
    first_number = input("Enter first number: ")
    second_number = input("Enter Second number: ")
    print("Difference is " + str(int(first_number) - int(second_number)))

elif operation == "3":
    first_number = input("Enter first number: ")
    second_number = input("Enter Second number: ")
    print("Product is " + str(int(first_number) * int(second_number)))

elif operation == "4":
    first_number = input("Enter first number: ")
    second_number = input("Enter Second number: ")
    print("Result is " + str(int(first_number) / int(second_number)))

elif operation == "5":
    first_number = input("Enter first number: ")
    second_number = input("Enter Second number: ")
    print("Modulo solution is " + str(int(first_number) % int(second_number)))

else:
    print("Invalid Entry")
