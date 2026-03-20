# 🐍 Python Mastery — AI & Machine Learning

> **Beginner → Job-Ready** | 60 Days · 8 Weeks · 6 Real Projects

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Progress](https://img.shields.io/badge/Progress-Day%206%20of%2060-22C55E?style=flat)](.)
[![Days Complete](https://img.shields.io/badge/Days%20Complete-6-6366f1?style=flat)](.)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)](.)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat)](.)

---

## 📖 About This Repository

This repository documents my **60-day structured journey** to master Python for AI & Machine Learning — from absolute beginner to job-ready developer.

Every day includes:
- ✅ Concept notes with code examples
- ✅ Practice exercises
- ✅ Mini projects
- ✅ Reference resources

---

## 🗺️ Learning Roadmap

| Phase | Weeks | Focus | Status |
|-------|-------|-------|--------|
| **Phase 1** | Week 1–2 | Python Core Fundamentals | 🔄 In Progress |
| **Phase 2** | Week 3–4 | Automation & Real Scripts | ⏳ Upcoming |
| **Phase 3** | Week 5–6 | Web Apps & AI/ML Basics | ⏳ Upcoming |
| **Phase 4** | Week 7–8 | Portfolio & Job Readiness | ⏳ Upcoming |

---

## 📁 Repository Structure

```
Python/
│
├── 📄 Python_AI_Mastery_Roadmap_60Days.docx   ← Full 60-day plan
│
├── 📂 Day1/                  ← Setup, Variables, Data Types, f-strings
│   ├── day1.py               ← Variables & types practice
│   ├── calculator.py         ← Day 1 project: basic calculator
│   └── README.md             ← Day 1 notes & guide
│
├── 📂 Day2/                  ← Control Flow & Loops
│   ├── day2.py               ← if/elif/else & loops practice
│   ├── calculator_v2.py      ← Day 2 project: calculator with menu
│   ├── guess_the_number.py   ← Bonus: number guessing game
│   └── README.md             ← Day 2 notes & guide
│
├── 📂 Day3/                  ← Functions — Reusable Code
│   ├── day3.py               ← def, params, return, scope practice
│   ├── functions_practice.py ← Day 3 project: function library
│   └── README.md             ← Day 3 notes & guide
│
├── 📂 Day4/                  ← Lists & Tuples — Ordered Collections
│   ├── day4.py               ← create, slice, methods practice
│   ├── list_practice.py      ← Day 4 project: grade tracker + matrix ops
│   └── README.md             ← Day 4 notes & guide
│
├── 📂 Day5/                  ← Dictionaries & Sets
│   ├── day5.py               ← dict/set creation, methods, comprehensions
│   ├── dict_practice.py      ← Day 5 project: student DB + word frequency
│   └── README.md             ← Day 5 notes & guide
│
├── 📂 Day6/                  ← Strings Deep Dive
│   ├── day6.py               ← string methods, slicing, regex practice
│   ├── text_analyzer.py      ← Day 6 project: text analyzer tool
│   └── README.md             ← Day 6 notes & guide
│
└── README.md                 ← This file
```

---

## 📅 Daily Progress

### 🔄 Week 1 — Python Core (6 / 7 days complete)

<details>
<summary><b>Day 1 — Setup, Variables & Data Types</b> ✅</summary>

**Topics covered:**
- Python 3.11+ installation & VS Code setup
- Variables: `int`, `float`, `str`, `bool`, `None`
- Type conversion: `int()`, `str()`, `float()`
- f-strings and string formatting

**Project:** Basic Calculator

```python
name = "Alice"
age = 25
print(f"Hello {name}, you are {age} years old!")
# Hello Alice, you are 25 years old!
```

📁 [View Day 1 →](./Day1/)

</details>

<details>
<summary><b>Day 2 — Control Flow & Loops</b> ✅</summary>

**Topics covered:**
- `if`, `elif`, `else` conditions
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- `for` loops + `range()`
- `while` loops + `break` / `continue`

**Project:** Calculator v2 with menu loop

```python
while True:
    choice = input("Choose operation (+, -, *, /) or 'q' to quit: ")
    if choice == 'q':
        break
    # ... calculation logic
```

📁 [View Day 2 →](./Day2/)

</details>

<details>
<summary><b>Day 3 — Functions: Reusable Code</b> ✅</summary>

**Topics covered:**
- `def` keyword, parameters, return values
- Default parameters, `*args`, `**kwargs`
- Scope: local vs global
- Lambda functions
- Docstrings and type hints (intro)

**Project:** Function Library

```python
def calculate_tax(price: float, rate: float = 0.18) -> float:
    """Calculate tax on a price.

    Args:
        price: The base price in rupees.
        rate: Tax rate (0–1). Default 18%.

    Returns:
        Tax amount as a float.
    """
    return price * rate

# Lambda as sort key
students = [{"name": "Alice", "grade": 88}, {"name": "Bob", "grade": 95}]
top = sorted(students, key=lambda s: s["grade"], reverse=True)
```

📁 [View Day 3 →](./Day3/)

</details>

<details>
<summary><b>Day 4 — Lists & Tuples: Ordered Collections</b> ✅</summary>

**Topics covered:**
- Create, access, slice lists — positive & negative indexing, `start:stop:step`
- List methods: `append`, `pop`, `extend`, `sort`, `reverse` — mutates vs returns new
- List comprehensions — the essential Python pattern for AI/ML data pipelines
- Tuples vs lists — immutability, unpacking, tuples as dict keys
- Nested lists — 2D arrays, `matrix[row][col]`, comprehension-built grids

**Project:** Student grade tracker + matrix operations

```python
# List comprehension — normalise data to 0-1 (used everywhere in ML)
raw = [10, 20, 30, 40, 50]
normalised = [(x - min(raw)) / (max(raw) - min(raw)) for x in raw]
# [0.0, 0.25, 0.5, 0.75, 1.0]

# Tuple unpacking
name, age, city = ("Alice", 25, "Chennai")
a, b = b, a   # swap without a temp variable

# 2D list — gateway to NumPy matrices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])   # 6  — row 1, col 2
```

📁 [View Day 4 →](./Day4/)

</details>

<details>
<summary><b>Day 5 — Dictionaries & Sets</b> ✅</summary>

**Topics covered:**
- Create, access, update dicts — `d["key"]`, `del`, `"key" in d`
- Dict methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, `.pop()`
- Dict comprehensions — filter, transform, invert, build from zip
- Sets — unique values, `|` `&` `-` `^` operations, O(1) membership test
- Nested dicts — JSON pattern, `json.loads()` / `json.dumps()`

**Project:** Student database + set operations + word frequency counter

```python
# Safe lookup — always prefer .get() over []
student.get("grade", "N/A")   # no KeyError if key missing

# Dict comprehension
discounted = {item: price * 0.9 for item, price in prices.items()}

# Set operations
python_devs & ml_devs    # intersection — know both
python_devs - ml_devs    # difference  — python only

# JSON round-trip
import json
data = json.loads('{"name": "Alice", "score": 88}')
print(data["name"])   # Alice
```

📁 [View Day 5 →](./Day5/)

</details>

<details>
<summary><b>Day 6 — Strings Deep Dive</b> ✅</summary>

**Topics covered:**
- String methods: `split`, `join`, `strip`, `replace`, `find` — text cleaning for AI/NLP pipelines
- String slicing mastery — `[start:stop:step]`, negative indexing, reversal trick
- Regular expressions intro (`re` module) — `search`, `findall`, `sub`, `match`
- Format strings for output — f-strings, `.format()`, `%` formatting, alignment & padding
- AI/NLP relevance: tokenization, pattern extraction, data cleaning

**Project:** Text Analyzer Tool

```python
import re

def analyze_text(text: str) -> dict:
    """Analyze text and return statistics."""
    cleaned   = text.strip().lower()
    words     = cleaned.split()
    sentences = re.split(r'[.!?]+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]

    word_freq: dict = {}
    for word in words:
        word = re.sub(r'[^a-z]', '', word)   # remove punctuation
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    emails    = re.findall(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b', text)
    urls      = re.findall(r'https?://\S+', text)
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "char_count"   : len(text),
        "word_count"   : len(words),
        "sentence_count": len(sentences),
        "unique_words" : len(word_freq),
        "top_5_words"  : top_words,
        "emails_found" : emails,
        "urls_found"   : urls,
    }

sample = """
Python is an amazing language. Python is used in AI, web, and data science.
Contact us at info@example.com or visit https://python.org for more details!
"""
result = analyze_text(sample)
for key, val in result.items():
    print(f"{key:<20}: {val}")
```

📁 [View Day 6 →](./Day6/)

</details>

<details>
<summary><b>Day 7 — File Handling</b> ⏳ Coming soon</summary>

- `open()`, `read()`, `write()`, `close()`
- `with` statement (context manager)
- Read/write CSV files manually
- `os` and `pathlib` modules

</details>

### ⏳ Week 2 — Python Core continued (Days 8–14)

<details>
<summary><b>Day 8 — Error Handling & Debugging</b> ⏳ Coming soon</summary>

- `try`, `except`, `finally`, `raise`
- Common errors: `TypeError`, `ValueError`, `KeyError`
- Debugging with `print()`, breakpoints, VS Code debugger

</details>

<details>
<summary><b>Day 9 — Modules, Packages & pip</b> ⏳ Coming soon</summary>
</details>

<details>
<summary><b>Day 10–11 — Object-Oriented Programming</b> ⏳ Coming soon</summary>
</details>

<details>
<summary><b>Day 12 — APIs & HTTP Requests</b> ⏳ Coming soon</summary>
</details>

<details>
<summary><b>Day 13 — Data Structures & Algorithms Basics</b> ⏳ Coming soon</summary>
</details>

<details>
<summary><b>Day 14 — Week Project: CLI Task Manager</b> ⏳ Coming soon</summary>
</details>

---

## 📊 Skills Unlocked

| Skill | Status | Day |
|-------|--------|-----|
| Variables & data types | ✅ Done | Day 1 |
| Type conversion & f-strings | ✅ Done | Day 1 |
| if / elif / else | ✅ Done | Day 2 |
| for & while loops | ✅ Done | Day 2 |
| break & continue | ✅ Done | Day 2 |
| Functions (`def`, `return`) | ✅ Done | Day 3 |
| Default params, `*args`, `**kwargs` | ✅ Done | Day 3 |
| Scope (local vs global) | ✅ Done | Day 3 |
| Lambda functions | ✅ Done | Day 3 |
| Type hints & docstrings | ✅ Done | Day 3 |
| Lists & tuples | ✅ Done | Day 4 |
| Slicing & indexing | ✅ Done | Day 4 |
| List comprehensions | ✅ Done | Day 4 |
| Tuple unpacking | ✅ Done | Day 4 |
| 2D nested lists | ✅ Done | Day 4 |
| Dictionaries & sets | ✅ Done | Day 5 |
| Dict comprehensions | ✅ Done | Day 5 |
| Set operations | ✅ Done | Day 5 |
| Nested dicts / JSON | ✅ Done | Day 5 |
| String methods & regex | ✅ Done | Day 6 |
| File I/O | ⏳ Day 7 | — |
| Error handling | ⏳ Day 8 | — |
| OOP | ⏳ Day 10–11 | — |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python_3.11+-3776AB?style=flat&logo=python&logoColor=white) | Core language |
| ![VS Code](https://img.shields.io/badge/-VS_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white) | Code editor |
| ![Git](https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white) | Version control |
| ![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white) | Portfolio hosting |

**Libraries (added as learning progresses):**

`pandas` · `numpy` · `matplotlib` · `scikit-learn` · `Flask` · `FastAPI` · `LangChain` · `TensorFlow`

---

## 🎯 6 Projects — By End of 60 Days

| # | Project | Skills | Status |
|---|---------|--------|--------|
| 01 | **CLI Task Manager** | OOP, File I/O, Error Handling | ⏳ Week 1–2 |
| 02 | **CSV Data Cleaner** | pandas, Automation | ⏳ Week 3–4 |
| 03 | **Data Analysis Pipeline** | pandas, matplotlib, seaborn | ⏳ Week 3–4 |
| 04 | **AI PDF Chatbot** | LangChain, LLMs, Streamlit | ⏳ Week 5–6 |
| 05 | **ML Model API** | scikit-learn, FastAPI, Docker | ⏳ Week 7–8 |
| 06 | **Capstone AI App** | Full Stack, Auth, DB, CI/CD | ⏳ Week 7–8 |

---

## 🚀 How to Run

### Prerequisites
- Python 3.11+
- VS Code with Python extension

### Setup

```bash
# Clone the repository
git clone https://github.com/Sathya-02/PythonMastery.git
cd Python

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies (added as project grows)
pip install -r requirements.txt
```

### Run any day's code

```bash
cd Day1
python calculator.py

cd ../Day2
python calculator_v2.py

cd ../Day3
python functions_practice.py

cd ../Day4
python list_practice.py

cd ../Day5
python dict_practice.py

cd ../Day6
python text_analyzer.py
```

---

## 📚 Key Resources

| Resource | Link |
|----------|------|
| Python Official Docs | [docs.python.org](https://docs.python.org/3/) |
| Real Python | [realpython.com](https://realpython.com/) |
| Automate the Boring Stuff | [automatetheboringstuff.com](https://automatetheboringstuff.com/) |
| Kaggle Learn | [kaggle.com/learn](https://www.kaggle.com/learn) |
| LeetCode | [leetcode.com](https://leetcode.com/) |
| HuggingFace | [huggingface.co](https://huggingface.co/) |

---

## 📈 Commit Activity

> Committing every day to build consistency and visible progress.

---

## 🤝 Connect

If you're on a similar journey, feel free to:
- ⭐ **Star** this repo to follow along
- 🍴 **Fork** it and adapt it to your own learning
- 💬 Open an **Issue** if you spot a bug or have a suggestion

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with consistency, one day at a time. 🐍**

*Day 6 of 60 complete — strings, slicing, regex, and text analysis unlocked.*

</div>
