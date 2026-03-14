# 🐍 Python Day 4 — Lists & Tuples: Ordered Collections

> **Phase 1 · Week 1 · Day 4** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- Create, access, and slice lists — positive & negative indexing
- List methods: `append`, `pop`, `extend`, `sort`, `reverse`
- List comprehensions — the essential pattern for AI/ML
- Tuples vs lists — when to use each
- Nested lists — 2D arrays intro (gateway to NumPy)
- **Practice Project:** Student grade tracker + matrix operations

---

## The Mental Model

A list is an ordered, mutable sequence. Think of it as a numbered row of boxes. Each box holds a value, each box has an index starting at **0**. Negative indices count from the end: `-1` is the last item, `-2` is second-to-last.

```
fruits = ["apple", "banana", "cherry"]
          index 0   index 1   index 2
          index -3  index -2  index -1
```

---

## Step 1: Create, Access, Slice

Create `day4.py` and type this out:

```python
# ── Creating lists ─────────────────────────────────────────────
fruits  = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed   = [1, "hello", True, 3.14, None]   # lists hold any type
empty   = []

# ── Accessing elements ─────────────────────────────────────────
print(fruits[0])    # "apple"   — first element
print(fruits[-1])   # "cherry"  — last element
print(fruits[-2])   # "banana"

# ── Slicing: list[start:stop:step] ─────────────────────────────
#   start = inclusive, stop = exclusive
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]  — from beginning
print(numbers[2:])    # [30, 40, 50]  — to end
print(numbers[::2])   # [10, 30, 50]  — every 2nd element
print(numbers[::-1])  # [50, 40, 30, 20, 10]  — reversed!

# ── Modify elements ────────────────────────────────────────────
fruits[1] = "blueberry"
print(fruits)         # ["apple", "blueberry", "cherry"]

# ── len(), in, not in ──────────────────────────────────────────
print(len(fruits))           # 3
print("apple" in fruits)     # True
print("mango" not in fruits) # True
```

---

## Step 2: List Methods

### Key difference to memorise — mutates vs returns new

| Mutates in-place (no return value) | Returns a new list (original unchanged) |
|---|---|
| `.append()` `.pop()` `.sort()` | `sorted(lst)` `reversed(lst)` |
| `.extend()` `.insert()` `.reverse()` `.remove()` | `lst[:]` `lst + other` |

> ⚠️ Common bug: `x = my_list.sort()` → `x` is `None`! Use `sorted(my_list)` instead.

```python
# ── append vs extend ───────────────────────────────────────────
fruits = ["apple", "banana"]

fruits.append("cherry")
print(fruits)               # ["apple", "banana", "cherry"]

fruits.append(["date", "elderberry"])   # ⚠️ adds the LIST as one item
print(fruits)               # ["apple", "banana", "cherry", ["date", "elderberry"]]

fruits2 = ["apple", "banana"]
fruits2.extend(["date", "elderberry"])  # ✅ merges items individually
print(fruits2)              # ["apple", "banana", "date", "elderberry"]

# ── pop ────────────────────────────────────────────────────────
nums = [10, 20, 30, 40]
last = nums.pop()           # removes & returns last element
print(last)   # 40
print(nums)   # [10, 20, 30]

second = nums.pop(1)        # removes & returns index 1
print(second) # 20
print(nums)   # [10, 30]

# ── sort ───────────────────────────────────────────────────────
scores = [85, 42, 91, 67, 55]
scores.sort()               # ascending, in-place
print(scores)               # [42, 55, 67, 85, 91]

scores.sort(reverse=True)   # descending
print(scores)               # [91, 85, 67, 55, 42]

names = ["Charlie", "Alice", "Bob"]
names.sort()                # alphabetical
names.sort(key=len)         # sort by string length
print(names)                # ["Bob", "Alice", "Charlie"]

# ── sorted() returns new — original unchanged ──────────────────
original   = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print(original)    # [3, 1, 4, 1, 5]  ← unchanged
print(new_sorted)  # [1, 1, 3, 4, 5]

# ── reverse ────────────────────────────────────────────────────
items = [1, 2, 3, 4, 5]
items.reverse()
print(items)       # [5, 4, 3, 2, 1]
```

---

## Step 3: List Comprehensions

The single most important Python pattern for AI/ML. Pandas, NumPy, and data pipelines use it constantly.

**Syntax:** `[expression  for variable in iterable  if condition]`

The `if condition` part is optional — use it to filter.

```python
# ── Basic comprehensions ───────────────────────────────────────
squares = [x**2 for x in range(10)]
print(squares)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ── Transform strings ─────────────────────────────────────────
words = ["hello", "WORLD", "Python"]
lower   = [w.lower() for w in words]
lengths = [len(w) for w in words]
print(lower)      # ["hello", "world", "python"]
print(lengths)    # [5, 5, 6]

# ── Filter with condition ─────────────────────────────────────
scores  = [45, 88, 72, 91, 55, 60, 83]
passing = [s for s in scores if s >= 60]
print(passing)    # [88, 72, 91, 60, 83]

# ── Real AI/ML usage — normalise to 0-1 range ─────────────────
raw = [10, 20, 30, 40, 50]
min_val, max_val = min(raw), max(raw)
normalised = [(x - min_val) / (max_val - min_val) for x in raw]
print(normalised) # [0.0, 0.25, 0.5, 0.75, 1.0]

# ── Flatten a 2D list ─────────────────────────────────────────
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [num for row in matrix for num in row]
print(flat)       # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ── Conditional expression (if/else inside expression) ────────
labels = ["pass" if s >= 60 else "fail" for s in scores]
print(labels)     # ["fail", "pass", "pass", "pass", "fail", "pass", "pass"]
```

---

## Step 4: Tuples vs Lists

| | List `[ ]` | Tuple `( )` |
|---|---|---|
| Mutability | Mutable — can change | Immutable — fixed forever |
| Use when | Collection grows/changes | Fixed record / coordinates |
| Dict key? | ❌ Not hashable | ✅ Yes, tuples are hashable |
| Speed | Slightly slower | Faster, less memory |
| Examples | `cart`, `scores`, `names` | `point`, `rgb`, `(lat, lon)` |

```python
# ── Creating tuples ────────────────────────────────────────────
point  = (10, 20)
rgb    = (255, 128, 0)
single = (42,)       # ⚠️ one-element tuple MUST have trailing comma
empty  = ()

# ── Access — same as lists ─────────────────────────────────────
print(point[0])    # 10
print(rgb[-1])     # 0

# ── Immutability ───────────────────────────────────────────────
point[0] = 99      # ❌ TypeError: 'tuple' object does not support item assignment

# ── Tuple unpacking ────────────────────────────────────────────
x, y = point
print(x, y)        # 10  20

name, age, city = ("Alice", 25, "Chennai")
print(name)        # Alice

# ── Swap without a temp variable ──────────────────────────────
a, b = 10, 20
a, b = b, a
print(a, b)        # 20  10

# ── Functions returning multiple values use tuples ────────────
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

lo, hi = min_max([3, 1, 7, 2, 9])
print(lo, hi)      # 1  9

# ── Tuples as dictionary keys ─────────────────────────────────
locations = {
    (13.08, 80.27): "Chennai",
    (28.61, 77.20): "Delhi",
}
print(locations[(13.08, 80.27)])   # "Chennai"
```

---

## Step 5: Nested Lists — 2D Arrays

This is the direct gateway to NumPy matrices used in all ML math.

Access syntax: `matrix[row][col]`

```python
# ── Create a 2D list ──────────────────────────────────────────
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# ── Access ────────────────────────────────────────────────────
print(matrix[0][0])   # 1  — top-left
print(matrix[1][2])   # 6  — row 1, col 2
print(matrix[2][-1])  # 9  — last item of last row

# ── Modify ────────────────────────────────────────────────────
matrix[0][1] = 99
print(matrix[0])      # [1, 99, 3]

# ── Iterate rows and columns ──────────────────────────────────
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()            # newline after each row

# ── Build a matrix with comprehension ─────────────────────────
grid = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print(grid)            # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# ── Extract a full column ─────────────────────────────────────
col_1 = [row[1] for row in matrix]
print(col_1)           # [99, 5, 8]

# ── ⚠️ Wrong way to create a 2D list ─────────────────────────
bad = [[0] * 3] * 3    # all rows share the SAME inner list!
bad[0][0] = 99
print(bad)             # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]  ← all rows changed!

# ✅ Correct way — comprehension creates independent rows
good = [[0] * 3 for _ in range(3)]
good[0][0] = 99
print(good)            # [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## Practice Project — Student Grade Tracker

Create `list_practice.py`:

```python
# list_practice.py — Day 4 project

# ── 1. Student grade tracker ──────────────────────────────────
students = [
    ("Alice", [88, 92, 79, 95]),
    ("Bob",   [72, 68, 85, 77]),
    ("Carol", [95, 98, 92, 100]),
]

print("=== Grade Report ===")
for name, grades in students:
    avg    = sum(grades) / len(grades)
    best   = max(grades)
    status = "Pass" if avg >= 75 else "Fail"
    print(f"{name:<8} avg={avg:.1f}  best={best}  [{status}]")

# ── 2. List comprehension pipeline ───────────────────────────
all_grades = [g for _, grades in students for g in grades]
passing    = [g for g in all_grades if g >= 75]
normalised = [(g - min(all_grades)) / (max(all_grades) - min(all_grades))
              for g in all_grades]

print(f"\nAll grades:  {sorted(all_grades)}")
print(f"Passing:     {sorted(passing, reverse=True)}")
print(f"Normalised:  {[round(n, 2) for n in normalised]}")

# ── 3. Simple 3x3 matrix operations ──────────────────────────
matrix     = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
doubled    = [[x * 2 for x in row] for row in matrix]
transposed = [[matrix[r][c] for r in range(3)] for c in range(3)]

print(f"\nOriginal:    {matrix}")
print(f"Doubled:     {doubled}")
print(f"Transposed:  {transposed}")
```

### Sample Output

```
=== Grade Report ===
Alice    avg=88.5  best=95  [Pass]
Bob      avg=75.5  best=85  [Pass]
Carol    avg=96.2  best=100 [Pass]

All grades:  [68, 72, 77, 79, 85, 88, 92, 92, 95, 95, 98, 100]
Passing:     [100, 98, 95, 95, 92, 92, 88, 85, 79, 77, 75]
Normalised:  [0.63, 0.25, 0.28, 0.72, 0.53, 0.0, ...]

Original:    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Doubled:     [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
Transposed:  [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

## 🚀 Bonus Challenges

```python
# 1. Remove all duplicates while preserving order
def deduplicate(lst):
    seen = []
    return [x for x in lst if x not in seen and not seen.append(x)]

print(deduplicate([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]

# 2. Rotate a list left by n positions
def rotate_left(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

print(rotate_left([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]

# 3. Chunk a list into groups of n
def chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(chunk([1, 2, 3, 4, 5, 6, 7], 3))  # [[1, 2, 3], [4, 5, 6], [7]]

# 4. Matrix diagonal
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)  # [1, 5, 9]
```

---

## 📋 Day 4 Summary

| Concept | Syntax | Notes |
|---|---|---|
| Create list | `x = [1, 2, 3]` | Square brackets |
| Access | `x[0]`, `x[-1]` | Negative counts from end |
| Slice | `x[1:4]`, `x[::2]` | start:stop:step |
| Append | `x.append(v)` | Mutates in-place |
| Extend | `x.extend(lst)` | Merges items individually |
| Pop | `x.pop()` / `x.pop(i)` | Removes & returns |
| Sort in-place | `x.sort()` | Returns `None`! |
| Sort new | `sorted(x)` | Original unchanged |
| Comprehension | `[expr for x in it if cond]` | Essential for AI/ML |
| Create tuple | `t = (1, 2, 3)` | Immutable |
| Single tuple | `t = (42,)` | Trailing comma required |
| Unpack | `a, b = (10, 20)` | Works on any iterable |
| 2D access | `m[row][col]` | Row first, then column |
| 2D build | `[[0]*n for _ in range(m)]` | Use comprehension, not `*` |

---

## 📚 Resources

- [Real Python — Lists & Tuples](https://realpython.com/python-lists-and-tuples/)
- [Python Docs — List Methods](https://docs.python.org/3/tutorial/datastructures.html)
- [Automate the Boring Stuff — Ch 4](https://automatetheboringstuff.com/2e/chapter4/)

---

## ➡️ What's Next — Day 5

Tomorrow: **Dictionaries & Sets** — key-value data structures that power JSON parsing, API responses, and feature engineering in ML.

```python
# Preview of Day 5
student = {"name": "Alice", "age": 25, "score": 88}
print(student["name"])           # Alice
print(student.get("grade", "N/A"))  # N/A — safe default

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

Keep building — lists and comprehensions are the foundation every data pipeline runs on. 🚀
