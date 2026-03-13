# 🐍 Python Day 3 — Functions: Reusable Code

> **Phase 1 · Week 1 · Day 3** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- `def` keyword, parameters, return values
- Default parameters, `*args`, `**kwargs`
- Scope: local vs global
- Lambda functions
- Docstrings and type hints (intro)
- **Practice Project:** Function Library

---

## Step 1: The `def` keyword — anatomy of a function

A function is a named, reusable block of code. You define it once with `def`, then call it as many times as you need.

```
def  greet  (name,  age):
 ↑     ↑       ↑         body is 4-space indented
 │     │       └── parameters (inputs)
 │     └── function name (you choose)
 └── keyword that starts a function
         return f"Hello {name}, you are {age} years old!"
                 ↑
                 return value (output sent back to caller)
```

### Code Example

```python
# Define the function — this does NOT run it yet
def greet(name, age):
    return f"Hello {name}, you are {age} years old!"

# Call the function — this runs it
message = greet("Alice", 25)
print(message)    # Hello Alice, you are 25 years old!

# Call it again with different values — that's the point of reusable code
print(greet("Sathya", 22))    # Hello Sathya, you are 22 years old!

# Function without a return value
def say_hello(name):
    print(f"Hi {name}!")   # prints directly, returns None implicitly

say_hello("Bob")   # Hi Bob!

# Function with no parameters
def print_divider():
    print("-" * 40)

print_divider()   # ----------------------------------------
```

### Key Rules

- `def` and the function name are always on line one, ending with `:`
- The body is indented 4 spaces — everything at that indent level is part of the function
- `return` sends a value back to the caller and exits the function immediately
- If there's no `return`, the function returns `None`

---

## Step 2: Default parameters, *args, **kwargs

### Default parameters

Default parameters let callers skip arguments — the default value is used when nothing is passed.

```python
def greet(name, language="English"):
    if language == "Tamil":
        return f"Vanakkam {name}!"
    return f"Hello {name}!"

greet("Alice")             # → Hello Alice!  (uses default)
greet("Sathya", "Tamil")  # → Vanakkam Sathya!

# ⚠️ Rule: defaults must come AFTER non-defaults
def bad(x=1, y):   # SyntaxError!
def good(x, y=1):  # ✅ correct
```

### *args — variable positional arguments

`*args` collects any number of positional arguments into a **tuple**.

```python
def add_all(*numbers):
    # numbers is a tuple of everything passed in
    return sum(numbers)

add_all(1, 2, 3)          # → 6
add_all(10, 20, 30, 40)   # → 100
add_all()                  # → 0  (empty tuple)

def print_items(*items):
    for item in items:     # iterate the tuple
        print(f"- {item}")

print_items("apple", "banana", "cherry")
# - apple
# - banana
# - cherry
```

### **kwargs — variable keyword arguments

`**kwargs` collects any number of keyword arguments into a **dictionary**.

```python
def build_profile(**details):
    # details is a dict of key=value pairs
    for key, value in details.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=25, city="Chennai")
# name: Alice
# age: 25
# city: Chennai

# Also useful for passing a dict to a function
data = {"name": "Bob", "role": "admin"}
build_profile(**data)   # unpack dict as kwargs
```

### Combined — the correct order

The order must always be: `normal → *args → defaults → **kwargs`

```python
def full_example(required, *args, option="default", **kwargs):
    print(f"required: {required}")
    print(f"extras:   {args}")
    print(f"option:   {option}")
    print(f"named:    {kwargs}")

full_example("hello", 1, 2, option="yes", x=10, y=20)
# required: hello
# extras:   (1, 2)
# option:   yes
# named:    {'x': 10, 'y': 20}
```

---

## Step 3: Scope — local vs global

Scope answers the question: "which code can see which variable?"

```
┌──────────────────────────── Global scope ──────────────────────────────┐
│  username = "Alice"   ← visible everywhere                            │
│                                                                         │
│  ┌── def greet(): ───────┐     ┌── def calculate(): ──────────────┐   │
│  │  message = "Hello"    │     │  result = 42                      │   │
│  │  (local — only here)  │  ✗  │  (local — only here)             │   │
│  │  can read username ✅ │     │  cannot see greet's locals        │   │
│  └───────────────────────┘     └──────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Code Examples

```python
# Global variable — defined at the top level of the file
username = "Alice"

def greet():
    # Local variable — created inside the function, dies when function ends
    message = "Hello"
    print(f"{message}, {username}!")  # ✅ can READ global variable

greet()          # Hello, Alice!
print(message)   # ❌ NameError: 'message' is not defined (local, not accessible)

# Modifying a global variable inside a function
counter = 0

def increment():
    global counter      # declare you want to modify the global
    counter += 1

increment()
increment()
print(counter)   # 2
```

### Best Practice — avoid global

```python
# ❌ Avoid modifying globals when possible
total = 0
def add_to_total(x):
    global total
    total += x    # side effect — hard to test and reason about

# ✅ Better: pass in, return out
def add(current_total, x):
    return current_total + x

total = add(total, 5)
total = add(total, 10)
print(total)   # 15
```

---

## Step 4: Lambda functions

A lambda is a small, anonymous (nameless) function written on a single line.

### Syntax

```python
lambda parameters: expression
```

### Code Examples

```python
# Regular function vs lambda — same result
def square(x):
    return x ** 2

square = lambda x: x ** 2

print(square(5))   # 25

# Lambda with two parameters
add = lambda x, y: x + y
print(add(3, 4))   # 7

# Where lambdas shine — as sort keys
words = ["banana", "apple", "kiwi", "cherry"]
words.sort(key=lambda w: len(w))    # sort by word length
print(words)   # ['kiwi', 'apple', 'banana', 'cherry']

# sorted() — returns new list
nums = [-3, 1, -7, 4, -2]
sorted_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_abs)   # [1, -2, -3, 4, -7]

# filter() — keep only items where lambda returns True
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)   # [0, 2, 4, 6, 8]

# map() — apply lambda to every item
doubled = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(doubled)   # [2, 4, 6, 8]
```

### When to use lambda vs `def`

| Use `lambda` | Use `def` |
|---|---|
| Logic fits on one line | More than one line of logic |
| Only needed once (e.g. as a sort key) | Needs to be reused |
| Passed directly into another function | Needs a docstring or type hints |
| `sorted(items, key=lambda x: x.age)` | `def calculate_tax(price, rate):` |

---

## Step 5: Docstrings and type hints

These two features make your code readable and professional.

### Type hints

```python
# Annotate what types go in and come out
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old!"

# Common type hint patterns
def process(
    items: list,          # a list
    count: int = 0,       # int with default
    label: str = "item"   # str with default
) -> dict:                # returns a dict
    ...

# For more complex types — use the typing module
from typing import List, Dict, Optional

def get_scores(names: List[str]) -> Dict[str, int]:
    return {name: 0 for name in names}

def find_user(user_id: int) -> Optional[str]:
    # Optional means it can return str OR None
    return None
```

### Docstrings — Google style (most common in Python/AI work)

```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in metres.

    Returns:
        BMI value as a float, rounded to 2 decimal places.

    Raises:
        ValueError: If height_m is zero or negative.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return round(weight_kg / (height_m ** 2), 2)

# Access the docstring programmatically
print(calculate_bmi.__doc__)   # prints the docstring
help(calculate_bmi)            # formatted help output
```

### Why this matters for AI/ML work

FastAPI uses type hints to automatically generate your API documentation. pandas, LangChain, and scikit-learn are all heavily type-annotated. Writing type hints from Day 3 builds the habit that makes you production-ready.

---

## Practice Project — Function Library

Create `functions_practice.py` combining all five concepts:

```python
# functions_practice.py — Day 3 Project

# 1. Basic function with return and type hints
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# 2. Default parameters
def create_user(name: str, role: str = "viewer", active: bool = True) -> dict:
    """Create a user profile dictionary.

    Args:
        name: The user's full name.
        role: Permission level. Default 'viewer'.
        active: Account status. Default True.

    Returns:
        A dict with name, role, and active fields.
    """
    return {"name": name, "role": role, "active": active}

# 3. *args — variable positional arguments
def total_score(*scores: float) -> float:
    """Return the total of any number of scores."""
    return sum(scores)

# 4. **kwargs — variable keyword arguments
def display_info(**details) -> None:
    """Print all key-value pairs passed in."""
    for key, value in details.items():
        print(f"  {key}: {value}")

# 5. Lambda — sort list of dicts by a field
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 95},
    {"name": "Carol", "grade": 72},
]
top_students = sorted(students, key=lambda s: s["grade"], reverse=True)

# 6. Scope — clean version using return instead of global
def track_call(func_name: str, call_count: int) -> int:
    """Log a function call and return the updated count."""
    call_count += 1
    print(f"Called: {func_name} (total: {call_count})")
    return call_count

# --- Run it ---
print(celsius_to_fahrenheit(100))           # 212.0
print(create_user("Sathya", role="admin"))  # {'name': 'Sathya', 'role': 'admin', 'active': True}
print(total_score(85, 92, 78, 95))          # 350.0

display_info(name="Alice", city="Chennai", skill="Python")

print("\nTop students by grade:")
for student in top_students:
    print(f"  {student['name']}: {student['grade']}")

calls = 0
calls = track_call("celsius_to_fahrenheit", calls)
calls = track_call("create_user", calls)
```

### Expected Output

```
212.0
{'name': 'Sathya', 'role': 'admin', 'active': True}
350.0
  name: Alice
  city: Chennai
  skill: Python

Top students by grade:
  Bob: 95
  Alice: 88
  Carol: 72
Called: celsius_to_fahrenheit (total: 1)
Called: create_user (total: 2)
```

---

## 🚀 Bonus Challenges

### Challenge 1 — Recursive function

```python
def factorial(n: int) -> int:
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)   # function calls itself!

print(factorial(5))   # 120  (5 × 4 × 3 × 2 × 1)
```

### Challenge 2 — Higher-order function

```python
def apply_twice(func, value):
    """Apply a function to a value twice."""
    return func(func(value))

double = lambda x: x * 2
print(apply_twice(double, 3))   # 12  (3 → 6 → 12)
```

### Challenge 3 — Refactor the calculator

```python
# Turn your Day 2 calculator into clean functions

def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b

def divide(a: float, b: float) -> float | str:
    """Return a / b, or error message if b is zero."""
    if b == 0:
        return "Error: division by zero"
    return a / b

def run_calculator():
    """Main calculator loop."""
    operations = {'+': add, '-': subtract, '/': divide}

    while True:
        choice = input("Operation (+, -, /) or 'q': ")
        if choice == 'q':
            break
        if choice not in operations:
            print("Invalid operation")
            continue
        a = float(input("First number: "))
        b = float(input("Second number: "))
        result = operations[choice](a, b)
        print(f"Result: {result}")

run_calculator()
```

---

## 📋 Day 3 Summary

| Concept | Syntax | Purpose |
|---|---|---|
| Define function | `def name(params):` | Create reusable block of code |
| Return value | `return value` | Send result back to caller |
| Default param | `def f(x, y=10):` | Make argument optional |
| Variable positional | `def f(*args):` | Accept any number of positional args → tuple |
| Variable keyword | `def f(**kwargs):` | Accept any number of keyword args → dict |
| Local variable | Defined inside `def` | Only visible inside that function |
| Global variable | Defined outside `def` | Visible everywhere |
| Modify global | `global x` inside `def` | Declare intent to modify global |
| Lambda | `lambda x: x * 2` | One-line anonymous function |
| Type hints | `def f(x: int) -> str:` | Annotate expected types |
| Docstring | `"""Google style."""` | Document what a function does |

---

## 📚 Resources

- [Real Python — Functions Guide](https://realpython.com/defining-your-own-python-function/)
- [Python Docs — Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python — Type Hints](https://realpython.com/python-type-checking/)
- [Google Python Style Guide — Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Corey Schafer — Functions (YouTube)](https://www.youtube.com/watch?v=9Os0o3wzS_I)

---

## ➡️ What's Next — Day 4

Tomorrow you'll learn **Lists & Tuples** — Python's most-used data structures.

```python
# Preview of Day 4
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.sort()

# List comprehension — the Python superpower
squares = [x**2 for x in range(10)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Functions + lists together is where Python starts feeling powerful. 🚀
