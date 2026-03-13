#calculatory.py, Day 1 practice project

print("=" *40)
print("             Calculator")
print("=" *40)

#get input as float, handles both int & float
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#perform all operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2

#division needs special handling
if num2 != 0:
    div = num1 / num2
    floor_div = num1 // num2
    mod = num1 % num2
else:
    div = "Cannot divide by zero"
    floor_div = "Cannot divide by zero"
    mod = "Cannot divide by zero"

#Display results using f' string
print(f"\n{'Results':^40}"  )   #center align
print("-" * 40)
print(f"Addition: {num1} + {num2} = {add}")
print(f"Subtraction: {num1} - {num2} = {sub}")
print(f"Multiplication: {num1} * {num2} = {mul}")
print(f"Division: {num1} / {num2} = {div}")
print(f"Floor Division: {num1} // {num2} = {floor_div}")
print(f"Modulus: {num1} % {num2} = {mod}")
print("-" * 40) 

