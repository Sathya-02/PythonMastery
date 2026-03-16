# 🐍 Python Day 5 — Dictionaries & Sets

> **Phase 1 · Week 1 · Day 5** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- Create, access, and update dictionaries
- Dict methods: `.keys()`, `.values()`, `.items()`, `.get()`
- Dict comprehensions
- Sets: union, intersection, difference
- Nested dicts — JSON preview
- **Practice Project:** Student database + word frequency counter

---

## The Mental Model

A dictionary maps **keys** to **values** — like a labelled lookup table. Unlike a list (find by position), you find things by name. Keys must be immutable (strings, numbers, tuples). Values can be anything.

```
student = { "name": "Alice",  "score": 88,  "city": "Chennai" }
              key → value       key → value    key → value
```

---

## Step 1: Create, Access, Update

Create `day5.py` and type this:

```python
# ── Creating a dictionary ──────────────────────────────────────
student = {
    "name":  "Alice",
    "age":   25,
    "score": 88,
    "city":  "Chennai"
}

# ── Accessing values ───────────────────────────────────────────
print(student["name"])     # "Alice"
print(student["score"])    # 88

# ── KeyError — the most common dict mistake ────────────────────
print(student["grade"])    # ❌ KeyError: 'grade' — key doesn't exist

# ── .get() — safe access with a default ───────────────────────
print(student.get("grade"))          # None   — no crash
print(student.get("grade", "N/A"))   # "N/A"  — custom default

# ── Adding new key-value pairs ────────────────────────────────
student["grade"] = "A"
print(student)

# ── Updating an existing value ────────────────────────────────
student["score"] = 95
print(student["score"])    # 95

# ── Deleting a key ────────────────────────────────────────────
del student["city"]

# ── Check if a key exists ─────────────────────────────────────
print("name" in student)     # True
print("city" in student)     # False

# ── len() ─────────────────────────────────────────────────────
print(len(student))          # 4
```

---

## Step 2: Dict Methods — keys(), values(), items(), get()

| Method | Returns | Use for |
|---|---|---|
| `.keys()` | All key names | Checking/iterating keys |
| `.values()` | All values | Summing, filtering values |
| `.items()` | (key, value) pairs | Looping over both |
| `.get(k, default)` | Value or default | Safe lookup, no KeyError |
| `.update(other)` | — | Merging another dict |
| `.pop(k)` | Removed value | Remove and return |
| `.setdefault(k, v)` | Value | Add key only if missing |

```python
student = {"name": "Alice", "age": 25, "score": 88}

# ── .keys() ───────────────────────────────────────────────────
for key in student.keys():
    print(key)            # name  age  score

# ── .values() ─────────────────────────────────────────────────
total = sum(v for v in student.values() if isinstance(v, int))
print(total)              # 113

# ── .items() — the one you'll use most in loops ───────────────
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alice
# age: 25
# score: 88

# ── .get() with default — always prefer over [] ───────────────
print(student.get("score", 0))     # 88  — key exists
print(student.get("grade", "N/A")) # "N/A" — key missing, no crash

# ── .update() — merge another dict in ────────────────────────
student.update({"grade": "A", "city": "Chennai"})

# ── .pop() — remove and return ────────────────────────────────
age = student.pop("age")
print(age)   # 25

# ── .setdefault() — add key only if it doesn't exist ─────────
student.setdefault("grade", "B")   # does nothing — grade already exists
student.setdefault("rank", 1)      # adds rank: 1
```

---

## Step 3: Dict Comprehensions

Same power as list comprehensions, but produces `key: value` pairs.

**Syntax:** `{key_expr: value_expr  for var in iterable  if condition}`

```python
# ── Basic dict comprehension ───────────────────────────────────
squares = {x: x**2 for x in range(6)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ── Transform an existing dict ────────────────────────────────
prices = {"apple": 50, "banana": 20, "cherry": 80}

discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)
# {"apple": 45.0, "banana": 18.0, "cherry": 72.0}

# ── Filter while building ──────────────────────────────────────
expensive = {item: price for item, price in prices.items() if price > 30}
print(expensive)
# {"apple": 50, "cherry": 80}

# ── Invert a dict (swap keys and values) ──────────────────────
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)
# {1: "a", 2: "b", 3: "c"}

# ── Real ML usage — word frequency counter ────────────────────
words = ["the", "cat", "sat", "on", "the", "mat", "the"]
freq  = {word: words.count(word) for word in set(words)}
print(freq)
# {"the": 3, "cat": 1, "sat": 1, "on": 1, "mat": 1}

# ── Build from two lists with zip ─────────────────────────────
keys   = ["name", "age", "city"]
values = ["Alice", 25, "Chennai"]
record = {k: v for k, v in zip(keys, values)}
print(record)
# {"name": "Alice", "age": 25, "city": "Chennai"}
```

---

## Step 4: Sets

A set is an **unordered collection of unique values** — duplicates are removed automatically. Sets are perfect for membership testing and mathematical operations.

```
A = {1, 2, 3, 4, 5}     B = {3, 4, 5, 6, 7}

A | B  (union)        → {1, 2, 3, 4, 5, 6, 7}
A & B  (intersection) → {3, 4, 5}
A - B  (difference)   → {1, 2}
A ^ B  (sym. diff.)   → {1, 2, 6, 7}
```

```python
# ── Creating sets ──────────────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# ── Duplicates are silently removed ───────────────────────────
nums = {1, 2, 2, 3, 3, 3, 4}
print(nums)   # {1, 2, 3, 4}

# ── Dedup a list ──────────────────────────────────────────────
raw    = [1, 2, 2, 3, 3, 4]
unique = list(set(raw))
print(unique)  # [1, 2, 3, 4]  ← order not guaranteed

# ── ⚠️ Empty set — must use set(), not {} ─────────────────────
empty_set  = set()    # ✅ correct
empty_dict = {}       # this is an empty DICT, not a set!

# ── Set operations ────────────────────────────────────────────
python_devs = {"Alice", "Bob", "Carol", "Dave"}
ml_devs     = {"Carol", "Dave", "Eve", "Frank"}

print(python_devs | ml_devs)   # union — everyone
print(python_devs & ml_devs)   # intersection — know both
print(python_devs - ml_devs)   # difference — python only, not ML
print(python_devs ^ ml_devs)   # sym. diff — one or the other, not both

# ── Membership test — much faster than list ───────────────────
print("Alice" in python_devs)    # True  — O(1) lookup
print("Eve"   in python_devs)    # False

# ── Subset / superset ─────────────────────────────────────────
print({3, 4} <= a)    # True  — {3,4} is a subset of a
print(a >= {1, 2})    # True  — a is a superset of {1,2}

# ── .add() and .discard() ─────────────────────────────────────
python_devs.add("Grace")
python_devs.discard("Bob")    # safe remove — no error if missing

# ── Method-style operations ───────────────────────────────────
print(a.union(b))            # same as a | b
print(a.intersection(b))     # same as a & b
print(a.difference(b))       # same as a - b
```

---

## Step 5: Nested Dicts — JSON Preview

Every API response, config file, and database record follows this nested dict pattern. `json.loads()` turns a JSON string into a Python dict instantly.

```python
# ── Nested dict — a user record ───────────────────────────────
user = {
    "id": 101,
    "name": "Alice",
    "scores": {
        "math":    92,
        "english": 87,
        "science": 95
    },
    "tags": ["python", "ml", "data"]
}

# ── Access nested values ───────────────────────────────────────
print(user["name"])                # "Alice"
print(user["scores"]["math"])      # 92
print(user["tags"][0])             # "python"

# ── Modify nested values ───────────────────────────────────────
user["scores"]["math"] = 98
user["tags"].append("fastapi")

# ── Safe nested access with .get() ────────────────────────────
print(user.get("scores", {}).get("history", "N/A"))  # "N/A" — no crash

# ── Iterate nested dict ───────────────────────────────────────
for subject, score in user["scores"].items():
    print(f"  {subject}: {score}")

# ── Real API pattern — list of dicts ──────────────────────────
students = [
    {"name": "Alice", "grade": "A", "score": 95},
    {"name": "Bob",   "grade": "B", "score": 82},
    {"name": "Carol", "grade": "A", "score": 91},
]

names  = [s["name"] for s in students]
top    = [s for s in students if s["grade"] == "A"]
ranked = sorted(students, key=lambda s: s["score"], reverse=True)

# ── JSON parsing ──────────────────────────────────────────────
import json

json_str = '{"name": "Alice", "score": 88, "active": true}'
data = json.loads(json_str)
print(data["name"])      # Alice
print(data["active"])    # True  ← JSON true → Python True

python_dict = {"name": "Bob", "score": 92}
print(json.dumps(python_dict, indent=2))
# {
#   "name": "Bob",
#   "score": 92
# }
```

---

## Practice Project — Student Database

Create `dict_practice.py`:

```python
# dict_practice.py — Day 5 project

# ── 1. Student database ───────────────────────────────────────
students = {
    "S001": {"name": "Alice",  "scores": [88, 92, 95], "city": "Chennai"},
    "S002": {"name": "Bob",    "scores": [72, 68, 79], "city": "Mumbai"},
    "S003": {"name": "Carol",  "scores": [95, 98, 91], "city": "Chennai"},
    "S004": {"name": "Dave",   "scores": [60, 55, 70], "city": "Delhi"},
}

print("=== Student Report ===")
for sid, info in students.items():
    avg   = sum(info["scores"]) / len(info["scores"])
    grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
    print(f"{sid} | {info['name']:<8} | avg={avg:.1f} | {grade} | {info['city']}")

# ── 2. Dict comprehension — top students ─────────────────────
averages     = {sid: sum(i["scores"]) / len(i["scores"]) for sid, i in students.items()}
top_students = {sid: avg for sid, avg in averages.items() if avg >= 85}
print("\nTop students:", top_students)

# ── 3. Set operations — city groups ──────────────────────────
chennai = {i["name"] for i in students.values() if i["city"] == "Chennai"}
all_s   = {i["name"] for i in students.values()}

print("\nChennai:", chennai)
print("Not Chennai:", all_s - chennai)

# ── 4. Word frequency (NLP preprocessing) ────────────────────
text  = "the cat sat on the mat and the cat sat"
words = text.split()
freq  = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("\nWord frequencies:")
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")
```

---

## 🚀 Bonus Challenges

```python
# 1. Count character frequency in a string
text = "mississippi"
char_freq = {c: text.count(c) for c in set(text)}
print(char_freq)  # {"m": 1, "i": 4, "s": 4, "p": 2}

# 2. Group students by grade using defaultdict
from collections import defaultdict

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob",   "grade": "B"},
    {"name": "Carol", "grade": "A"},
]
by_grade = defaultdict(list)
for s in students:
    by_grade[s["grade"]].append(s["name"])
print(dict(by_grade))  # {"A": ["Alice", "Carol"], "B": ["Bob"]}

# 3. Flatten nested dict to dot-notation keys
def flatten(d, prefix=""):
    result = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.update(flatten(v, key))
        else:
            result[key] = v
    return result

nested = {"user": {"name": "Alice", "scores": {"math": 92}}}
print(flatten(nested))
# {"user.name": "Alice", "user.scores.math": 92}
```

---

## 📋 Day 5 Summary

| Concept | Syntax | Notes |
|---|---|---|
| Create dict | `d = {"key": val}` | Key must be immutable |
| Access | `d["key"]` | KeyError if missing |
| Safe access | `d.get("key", default)` | Returns default, no crash |
| Add/update | `d["key"] = val` | Creates or overwrites |
| Delete | `del d["key"]` | KeyError if missing |
| All keys | `d.keys()` | Iterable view |
| All values | `d.values()` | Iterable view |
| Key-value pairs | `d.items()` | Use in for loops |
| Merge | `d.update(other)` | Overwrites on conflict |
| Dict comprehension | `{k: v for k, v in ...}` | Filter with `if` |
| Create set | `s = {1, 2, 3}` | Empty set: `set()` |
| Union | `a \| b` | All unique elements |
| Intersection | `a & b` | Elements in both |
| Difference | `a - b` | In a, not in b |
| Membership | `x in s` | O(1) — very fast |
| JSON parse | `json.loads(str)` | String → dict |
| JSON dump | `json.dumps(d)` | Dict → string |

---

## 📚 Resources

- [Real Python — Dictionaries](https://realpython.com/python-dicts/)
- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [W3Schools — Python Sets](https://www.w3schools.com/python/python_sets.asp)

---

## ➡️ What's Next — Day 6

Tomorrow: **Strings Deep Dive** — methods, slicing, and an intro to regular expressions.

```python
# Preview of Day 6
text = "  Hello, World!  "
print(text.strip())          # "Hello, World!"
print(text.lower())          # "  hello, world!  "
print(text.split(", "))      # ["  Hello", "World!  "]
print(", ".join(["a","b"]))  # "a, b"

import re
emails = re.findall(r'\S+@\S+', "contact alice@example.com or bob@test.org")
print(emails)  # ["alice@example.com", "bob@test.org"]
```

Keep going — dicts and sets are the backbone of every data pipeline, API handler, and NLP task you'll write. 🚀
