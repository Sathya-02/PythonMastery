# 🐍 Python Day 1 — Setup, Variables, Types & f-strings

> **Phase 1 · Week 1 · Day 1** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- Install Python, VS Code, configure interpreter
- Variables: `int`, `float`, `str`, `bool`, `None`
- Type conversion: `int()`, `str()`, `float()`
- f-strings and string formatting
- **Practice Project:** Calculator program

---

## Step 1: Install Python

Go to **https://python.org/downloads** → download Python 3.11+ → run the installer.

> ⚠️ **Critical (Windows users):** Check ✅ **"Add Python to PATH"** before clicking Install. Without this, Python won't work in the terminal.

### Verify Installation

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
python --version
```

You should see something like:

```
Python 3.11.x
```

---

## Step 2: Install VS Code

1. Go to **https://code.visualstudio.com** → download → install
2. Open VS Code
3. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)
4. Search **"Python"** → install the extension by **Microsoft**

### Configure the Interpreter

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type **"Python: Select Interpreter"**
3. Choose the **Python 3.11+** version you just installed

> ✅ You'll see the Python version in the bottom-left status bar of VS Code once configured.

---

## Step 3: Variables & Data Types

Create a new file in VS Code called `day1.py`.

Python has **5 core data types** you'll use constantly:

| Type | What it stores | Example |
|------|---------------|---------|
| `int` | Whole numbers | `age = 25` |
| `float` | Decimal numbers | `price = 9.99` |
| `str` | Text / strings | `name = "Alice"` |
| `bool` | True or False | `active = True` |
| `None` | No value / empty | `result = None` |

### Code — Type this into `day1.py`

```python
# Variables — Python figures out the type automatically
age = 25             # int
price = 9.99         # float
name = "Alice"       # str
is_active = True     # bool
result = None        # None (no value yet)

# Check types
print(type(age))         # <class 'int'>
print(type(price))       # <class 'float'>
print(type(name))        # <class 'str'>
print(type(is_active))   # <class 'bool'>
print(type(result))      # <class 'NoneType'>

# Print values
print(age)               # 25
print(price)             # 9.99
print(name)              # Alice
print(is_active)         # True
print(result)            # None
```

**Run it:** Press the green ▶ button in VS Code, or type `python day1.py` in the terminal.

### Key Rules for Variables

```python
# ✅ Valid variable names
user_name = "Alice"      # snake_case (preferred in Python)
age2 = 30
_private = "hidden"

# ❌ Invalid variable names
2age = 30                # cannot start with a number
my-name = "Alice"        # hyphens not allowed
class = "Maths"          # 'class' is a reserved keyword
```

---

## Step 4: Type Conversion

You'll constantly need to convert between types — especially when reading user input (which is **always a string**).

### The Three Core Conversion Functions

```python
int()      # converts to integer (whole number)
float()    # converts to decimal number
str()      # converts to string (text)
```

### Code Examples

```python
# String to number
age_str = "25"
age_int = int(age_str)       # "25" → 25
age_float = float(age_str)   # "25" → 25.0

# Number to string
num = 100
num_str = str(num)           # 100 → "100"

# Float to int (truncates — does NOT round)
pi = 3.99
pi_int = int(pi)             # 3.99 → 3  (not 4!)

print(type(age_str))         # <class 'str'>
print(type(age_int))         # <class 'int'>
print(type(age_float))       # <class 'float'>
print(type(num_str))         # <class 'str'>
```

### ⚠️ The Most Common Beginner Mistake

```python
# input() ALWAYS returns a string — even if the user types a number

# ❌ Wrong — this will crash when you try to do math
age = input("Enter your age: ")
next_year = age + 1          # TypeError: can only concatenate str (not "int") to str

# ✅ Correct — convert immediately
age = int(input("Enter your age: "))
next_year = age + 1          # Works! → 26
print(f"Next year you'll be {next_year}")
```

### Conversion Errors to Know

```python
# These will raise a ValueError
int("hello")       # ValueError: invalid literal for int()
float("abc")       # ValueError: could not convert string to float
int("3.14")        # ValueError: invalid literal (use float() first, then int())

# Safe way — convert float string to int
value = int(float("3.14"))   # → 3  ✅
```

---

## Step 5: f-strings (String Formatting)

f-strings are the **modern, clean way** to embed variables inside text. They're used everywhere in Python code.

**Syntax:** Put `f` before the opening quote. Use `{}` to embed any variable or expression.

```python
f"Your text {variable} more text"
```

### Basic f-strings

```python
name = "Alice"
age = 25
city = "Chennai"

# Embed variables
print(f"Hello, {name}!")                  # Hello, Alice!
print(f"You are {age} years old.")        # You are 25 years old.
print(f"{name} lives in {city}.")         # Alice lives in Chennai.

# Math inside f-strings
print(f"Next year you'll be {age + 1}.") # Next year you'll be 26.
print(f"Is adult: {age >= 18}")           # Is adult: True
```

### Number Formatting in f-strings

```python
score = 98.567
pi = 3.14159
big_num = 1000000

# Decimal places
print(f"Score: {score:.2f}")              # Score: 98.57
print(f"Score: {score:.0f}%")            # Score: 99%
print(f"Pi: {pi:.4f}")                   # Pi: 3.1416

# Thousands separator
print(f"Population: {big_num:,}")         # Population: 1,000,000

# Padding and alignment
print(f"{'Left':<10}|")                  # Left      |
print(f"{'Right':>10}|")                 #      Right|
print(f"{'Center':^10}|")               #   Center  |

# Width and fill
print(f"{42:05d}")                        # 00042  (pad with zeros)
```

### Older Formatting Styles (you'll see in old code)

```python
name = "Alice"
score = 95.5

# % formatting — old style, avoid
print("Hello, %s! Score: %.1f" % (name, score))

# .format() — older style, avoid
print("Hello, {}! Score: {:.1f}".format(name, score))

# f-string — modern, use this ✅
print(f"Hello, {name}! Score: {score:.1f}")
```

---

## Step 6: Practice Project — Calculator Program

Now put everything together. Create a new file called `calculator.py`.

> 💡 **Tip:** Type this out — don't copy-paste. Typing builds muscle memory.

```python
# calculator.py — Day 1 Practice Project

print("=" * 40)
print("       Simple Python Calculator")
print("=" * 40)

# Get input and convert to float (handles both int and decimal numbers)
num1 = float(input("\nEnter first number:  "))
num2 = float(input("Enter second number: "))

# Perform all operations
addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2

# Division needs special handling — can't divide by zero
if num2 != 0:
    division  = num1 / num2
    floor_div = num1 // num2    # whole number division (drops decimal)
    remainder = num1 % num2     # modulo — the leftover after division
else:
    division = floor_div = remainder = "undefined (division by zero)"

# Display results using f-strings
print(f"\n{'Results':^40}")     # centered heading in 40-char wide field
print("-" * 40)
print(f"  {num1} + {num2}  =  {addition}")
print(f"  {num1} - {num2}  =  {subtraction}")
print(f"  {num1} × {num2}  =  {multiplication}")
print(f"  {num1} ÷ {num2}  =  {division}")
print(f"  {num1} // {num2} =  {floor_div}  (floor division)")
print(f"  {num1} % {num2}  =  {remainder}  (remainder)")
print("-" * 40)
```

### Sample Output

```
========================================
       Simple Python Calculator
========================================

Enter first number:  10
Enter second number: 3

             Results
----------------------------------------
  10.0 + 3.0  =  13.0
  10.0 - 3.0  =  7.0
  10.0 × 3.0  =  30.0
  10.0 ÷ 3.0  =  3.3333333333333335
  10.0 // 3.0 =  3.0  (floor division)
  10.0 % 3.0  =  1.0  (remainder)
----------------------------------------
```

### Test These Inputs

| num1 | num2 | What to observe |
|------|------|-----------------|
| `10` | `3` | Decimal division, floor div, remainder |
| `7.5` | `2.5` | Float arithmetic |
| `5` | `0` | Division by zero protection |
| `-10` | `3` | Negative number behaviour |

---

## 🚀 Bonus Challenge

Extend your calculator with these additions once the basic version works:

```python
# 1. Show results rounded to 2 decimal places
print(f"  {num1} ÷ {num2}  =  {division:.2f}")

# 2. Show the data types of the inputs
print(f"\nnum1 is type: {type(num1).__name__}")
print(f"num2 is type: {type(num2).__name__}")

# 3. Add power and square root
import math
power = num1 ** num2
sqrt1 = math.sqrt(abs(num1))

print(f"  {num1} ^ {num2}  =  {power}")
print(f"  √{num1}       =  {sqrt1:.4f}")
```

---

## 📋 Day 1 Summary

| Concept | Syntax | Example |
|---------|--------|---------|
| Integer | `x = 25` | `age = 25` |
| Float | `x = 9.99` | `price = 9.99` |
| String | `x = "text"` | `name = "Alice"` |
| Boolean | `x = True` | `active = True` |
| None | `x = None` | `result = None` |
| Check type | `type(x)` | `type(age)` → `<class 'int'>` |
| To int | `int(x)` | `int("25")` → `25` |
| To float | `float(x)` | `float("9.99")` → `9.99` |
| To string | `str(x)` | `str(25)` → `"25"` |
| f-string | `f"Hi {var}"` | `f"Hello {name}!"` |
| Format decimal | `f"{x:.2f}"` | `f"{pi:.2f}"` → `"3.14"` |

---

## 📚 Resources

- [Python Official Docs — Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Real Python — Python Basics](https://realpython.com/python-first-steps/)
- [W3Schools Python Intro](https://www.w3schools.com/python/python_intro.asp)
- [Real Python — f-strings](https://realpython.com/python-f-strings/)

---

## ➡️ What's Next — Day 2

Tomorrow you'll learn **Control Flow** — `if/elif/else` and loops.

You'll upgrade this calculator to have a menu so users can choose which operation to perform, and loop until they decide to quit.

```python
# Preview of Day 2
while True:
    choice = input("Choose operation (+, -, *, /) or 'q' to quit: ")
    if choice == 'q':
        break
    elif choice == '+':
        # ... your addition logic here
```

Keep going — you're building the foundation everything else sits on. 🚀
