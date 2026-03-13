# 🐍 Python Day 2 — Control Flow: if/elif/else, Loops, break & continue

> **Phase 1 · Week 1 · Day 2** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- `if`, `elif`, `else` conditions
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- `for` loops + `range()`
- `while` loops + `break` / `continue`
- **Practice Project:** Upgraded Calculator with menu loop

---

## Step 1: if / elif / else — Making Decisions

The `if` statement lets your program choose what to do based on a condition. Python reads your conditions top to bottom and executes only the **first one that is `True`**.

### Syntax

```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if the first was False but this is True
else:
    # runs if nothing above was True
```

### Code Example

```python
score = 75

if score >= 90:
    print("A grade")
elif score >= 70:
    print("B grade")   # ← this runs because 75 >= 70
elif score >= 50:
    print("C grade")
else:
    print("Fail")
```

### How it flows

```
score = 75
    ↓
Is score >= 90?  → No
    ↓
Is score >= 70?  → Yes → print("B grade") → STOP (rest skipped)
```

### Key Rules

```python
# ✅ 'if' is mandatory — starts the block
# ✅ 'elif' is optional — you can have many
# ✅ 'else' is optional — catches everything that didn't match
# ✅ Indentation (4 spaces) defines what belongs to each block

# One-liner if (only for simple cases)
status = "adult" if age >= 18 else "minor"
```

### Common Mistakes

```python
# ❌ Missing colon
if score >= 90      # SyntaxError: expected ':'

# ❌ Wrong indentation
if score >= 90:
print("A grade")    # IndentationError

# ✅ Correct
if score >= 90:
    print("A grade")
```

---

## Step 2: Comparison Operators

These are the building blocks of every condition. They always return `True` or `False`.

| Operator | Meaning | Example (a=5, b=3) | Result |
|---|---|---|---|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>` | Greater than | `a > b` | `True` |
| `<` | Less than | `a < b` | `False` |
| `>=` | Greater than or equal | `a >= 5` | `True` |
| `<=` | Less than or equal | `a <= 3` | `False` |

### Code Examples

```python
age = 18

print(age == 18)   # True  — is age equal to 18?
print(age != 20)   # True  — is age NOT 20?
print(age > 21)    # False — is age greater than 21?
print(age < 21)    # True  — is age less than 21?
print(age >= 18)   # True  — is age 18 OR more?
print(age <= 17)   # False — is age 17 OR less?
```

### ⚠️ Critical Difference: `=` vs `==`

```python
age = 18       # ASSIGNMENT — sets the variable to 18
age == 18      # COMPARISON — asks "is age equal to 18?", returns True/False

# This is one of the most common beginner bugs:
if age = 18:   # ❌ SyntaxError — you can't assign inside if
if age == 18:  # ✅ Correct comparison
```

### Chaining Comparisons (Pythonic)

```python
# You can chain comparisons just like in maths
score = 75
print(50 <= score < 90)   # True — is 50 ≤ score < 90?

age = 20
print(18 <= age <= 65)    # True — is age between 18 and 65?
```

---

## Step 3: Logical Operators

Use `and`, `or`, `not` to combine multiple conditions into one.

### and — Both Must Be True

```
True  and True  → True
True  and False → False
False and True  → False
False and False → False
```

### or — At Least One Must Be True

```
True  or True  → True
True  or False → True
False or True  → True
False or False → False
```

### not — Flips the Value

```
not True  → False
not False → True
```

### Code Examples

```python
age = 20
has_id = True
is_member = False

# and — both conditions must be True
if age >= 18 and has_id:
    print("Entry allowed")       # ← prints this

# or — at least one condition must be True
if age >= 18 or is_member:
    print("Welcome")             # ← prints this (age >= 18 is True)

# not — flips True to False and vice versa
if not is_member:
    print("You are not a member")  # ← prints this

# Combining all three
if age >= 18 and has_id and not is_member:
    print("New adult visitor")   # ← prints this
```

### Operator Precedence (evaluation order)

```python
# not is evaluated first, then and, then or
result = True or False and not False
# Step 1: not False → True
# Step 2: False and True → False
# Step 3: True or False → True
print(result)  # True

# Use parentheses when in doubt — clearer and safer
result = (True or False) and (not False)
print(result)  # True
```

### Real-World Example

```python
username = "alice"
password = "secret123"
is_admin = True

# Login check
if username == "alice" and password == "secret123":
    if is_admin:
        print("Welcome, admin!")
    else:
        print("Welcome, user!")
else:
    print("Invalid credentials")
```

---

## Step 4: for Loops + range()

A `for` loop repeats a block of code for each item in a sequence. `range()` generates a sequence of numbers for you to loop over.

### range() Patterns

```python
range(5)         # → 0, 1, 2, 3, 4        (0 to n-1)
range(1, 6)      # → 1, 2, 3, 4, 5        (start to stop-1)
range(0, 10, 2)  # → 0, 2, 4, 6, 8        (start, stop, step)
range(10, 0, -1) # → 10, 9, 8, ..., 1     (countdown)
```

### Basic for Loop

```python
# Loop 5 times
for i in range(5):
    print(i)    # prints: 0 1 2 3 4

# Loop from 1 to 5
for i in range(1, 6):
    print(i)    # prints: 1 2 3 4 5

# Loop with step
for i in range(0, 10, 2):
    print(i)    # prints: 0 2 4 6 8

# Countdown
for i in range(5, 0, -1):
    print(i)    # prints: 5 4 3 2 1
```

### Looping Over Lists and Strings

```python
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)     # prints each fruit on a new line

# Loop over a string (character by character)
for char in "Python":
    print(char)      # prints: P y t h o n

# Loop with index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start enumerate from 1 (not 0)
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

### Practical Examples

```python
# Sum numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i           # same as: total = total + i
print(f"Sum 1-10: {total}")  # Sum 1-10: 55

# Multiplication table
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")

# Find even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i)         # prints: 2 4 6 8 10 12 14 16 18 20

# List comprehension (advanced but common — remember this!)
squares = [i**2 for i in range(1, 6)]
print(squares)           # [1, 4, 9, 16, 25]
```

---

## Step 5: while Loops + break / continue

A `while` loop keeps running **as long as its condition is `True`**. Use it when you don't know in advance how many times to loop.

### Basic while Loop

```python
count = 0
while count < 5:
    print(count)   # prints 0 1 2 3 4
    count += 1     # ⚠️ always update the variable or you get infinite loop!
```

### ⚠️ Infinite Loop — The Danger

```python
# ❌ This runs forever — never updating count!
count = 0
while count < 5:
    print(count)
    # forgot count += 1 — press Ctrl+C to stop

# ✅ Always ensure the condition will eventually be False
count = 0
while count < 5:
    print(count)
    count += 1    # ← this is critical
```

### break — Exit the Loop Early

```python
# Stop as soon as we find the number 3
number = 0
while True:           # would run forever without break
    if number == 3:
        break         # exits the loop immediately
    print(number)
    number += 1
# Output: 0 1 2
# (3 is never printed — break fires before the print)

# Practical: search in a list
names = ["Alice", "Bob", "Charlie", "Dave"]
search = "Charlie"
for name in names:
    if name == search:
        print(f"Found: {name}")
        break          # stop searching once found
```

### continue — Skip to the Next Iteration

```python
# Skip printing 3
for i in range(6):
    if i == 3:
        continue       # jump back to top of loop
    print(i)
# Output: 0 1 2 4 5   (3 is skipped)

# Skip negative numbers
numbers = [-2, 5, -1, 8, 3, -4, 7]
for num in numbers:
    if num < 0:
        continue       # skip negatives
    print(num)         # prints: 5 8 3 7
```

### Real-World while Pattern — Input Validation

```python
# Keep asking until valid input is given
while True:
    age_input = input("Enter your age (1-120): ")

    if age_input.isdigit() and 1 <= int(age_input) <= 120:
        age = int(age_input)
        print(f"Your age is {age}")
        break           # valid input received — exit
    else:
        print("Invalid! Please enter a number between 1 and 120.")
```

### for vs while — When to Use Which

| Use `for` when... | Use `while` when... |
|---|---|
| You know how many times to loop | You don't know how many times |
| Looping over a list, string, range | Waiting for user input |
| Iterating through data | Looping until a condition changes |
| `for i in range(10):` | `while user_input != 'q':` |

---

## Practice Project — Calculator v2 with Menu Loop

Upgrade your Day 1 calculator. Create `calculator_v2.py`:

```python
# calculator_v2.py — Day 2 Practice Project
# Combines: while loops, if/elif/else, break, continue, comparison + logical operators

print("=" * 40)
print("     Python Calculator v2")
print("=" * 40)

while True:                   # loop keeps running until user quits
    print("\nOperations: +  -  *  /  //  %  **")
    choice = input("Choose an operation (or 'q' to quit): ").strip()

    # Exit condition
    if choice == 'q':
        print("Goodbye!")
        break                 # exits the while loop

    # Validate operation
    valid_ops = ['+', '-', '*', '/', '//', '%', '**']
    if choice not in valid_ops:
        print("Invalid operation! Try again.")
        continue              # skip the rest, go back to top of while

    # Get numbers
    num1 = float(input("Enter first number:  "))
    num2 = float(input("Enter second number: "))

    # Calculate based on choice
    if choice == '+':
        result = num1 + num2
    elif choice == '-':
        result = num1 - num2
    elif choice == '*':
        result = num1 * num2
    elif choice == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            continue
        result = num1 / num2
    elif choice == '//':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            continue
        result = num1 // num2
    elif choice == '%':
        result = num1 % num2
    elif choice == '**':
        result = num1 ** num2

    print(f"\n  {num1} {choice} {num2} = {result}")
```

### Sample Session

```
========================================
     Python Calculator v2
========================================

Operations: +  -  *  /  //  %  **
Choose an operation (or 'q' to quit): +
Enter first number:  10
Enter second number: 5
  10.0 + 5.0 = 15.0

Operations: +  -  *  /  //  %  **
Choose an operation (or 'q' to quit): /
Enter first number:  8
Enter second number: 0
Error: Cannot divide by zero!

Operations: +  -  *  /  //  %  **
Choose an operation (or 'q' to quit): q
Goodbye!
```

---

## 🚀 Bonus Challenges

### Challenge 1 — Guess the Number Game

```python
import random

secret = random.randint(1, 100)
attempts = 0

print("Guess the number (1-100)!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break
```

### Challenge 2 — FizzBuzz (classic interview question)

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Challenge 3 — Prime Number Checker

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 50):
    if is_prime(num):
        print(num, end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

---

## 📋 Day 2 Summary

| Concept | Syntax | Purpose |
|---|---|---|
| `if` | `if condition:` | Run code if condition is True |
| `elif` | `elif condition:` | Check another condition |
| `else` | `else:` | Fallback if nothing matched |
| `==` | `a == b` | Equal to |
| `!=` | `a != b` | Not equal to |
| `>` `<` | `a > b` | Greater / less than |
| `>=` `<=` | `a >= b` | Greater / less or equal |
| `and` | `a and b` | Both must be True |
| `or` | `a or b` | At least one must be True |
| `not` | `not a` | Flip True ↔ False |
| `for` | `for i in range(n):` | Loop a known number of times |
| `while` | `while condition:` | Loop until condition is False |
| `break` | `break` | Exit the loop immediately |
| `continue` | `continue` | Skip to the next iteration |

---

## 📚 Resources

- [Python Official — Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Real Python — Python for Loop](https://realpython.com/python-for-loop/)
- [Real Python — Python while Loop](https://realpython.com/python-while-loop/)
- [Automate the Boring Stuff — Ch 2](https://automatetheboringstuff.com/2e/chapter2/)

---

## ➡️ What's Next — Day 3

Tomorrow you'll learn **Functions** — how to write reusable blocks of code.

You'll turn today's calculator into a set of clean functions, and learn about parameters, return values, and scope.

```python
# Preview of Day 3
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

result = add(10, 5)
print(result)    # 15
```

Keep building — control flow is the engine behind every program you'll ever write. 🚀
