#calculator v2
print("-" * 40)
print("            Calculator")
print("-" * 40)

while True:
    print("\n Operations: + - * / % // **")

    choice = input("Enter operation (or 'q' to quit): ").strip()

    if choice == 'q':
        break
    elif choice not in ('+', '-', '*', '/', '%', '//', '**'):
        print("Invalid operation. Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        result = num1 + num2
    elif choice == '-':
        result = num1 - num2
    elif choice == '*':
        result = num1 * num2
    elif choice == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            continue
    elif choice == '%':
        result = num1 % num2
    elif choice == '//':
        result = num1 // num2
    elif choice == '**':
        result = num1 ** num2

    print(f"Result: {num1} {choice} {num2} = {result}")  

