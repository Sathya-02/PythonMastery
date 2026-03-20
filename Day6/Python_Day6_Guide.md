# 🐍 Python Day 6 — Strings Deep Dive

> **Phase 1 · Week 1 · Day 6** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- String methods: `split`, `join`, `strip`, `replace`, `find`
- String slicing mastery — `[start:stop:step]`, negative indexing, reversal
- Regular expressions intro (`re` module) — `search`, `findall`, `sub`, `match`
- Format strings for output — f-strings, alignment, padding, number formatting
- **Practice Project:** Text analyzer tool

---

## The Mental Model

A Python string is an **immutable sequence of characters** — every character has a position (index), and you can slice, search, and transform it just like a list, but strings never change in place. Every method returns a **new string**.

```
s = "Python"
      ↑↑↑↑↑↑
      012345   ← positive indices
     -6-5-4-3-2-1 ← negative indices
```

---

## Step 1: String Methods — split, join, strip, replace, find

Create `day6.py` and type this:

```python
# ── split — break a string into a list ────────────────────────
sentence = "Python is great for AI and ML"
words = sentence.split()              # split on any whitespace
print(words)
# ['Python', 'is', 'great', 'for', 'AI', 'and', 'ML']

csv_line = "Alice,25,Chennai,Developer"
fields = csv_line.split(",")          # split on comma
print(fields)
# ['Alice', '25', 'Chennai', 'Developer']

# split with maxsplit — stop after N splits
first_two = sentence.split(" ", 2)
print(first_two)
# ['Python', 'is', 'great for AI and ML']

# ── join — reverse of split; glue list into string ────────────
words = ["Python", "is", "great"]
result = " ".join(words)              # join with space
print(result)
# 'Python is great'

csv_out = ",".join(["Alice", "25", "Chennai"])
print(csv_out)
# 'Alice,25,Chennai'

path = "/".join(["home", "user", "documents", "file.txt"])
print(path)
# 'home/user/documents/file.txt'

# ── strip — remove leading/trailing whitespace or chars ───────
raw = "   Hello, Python!   "
print(raw.strip())        # 'Hello, Python!'   — both sides
print(raw.lstrip())       # 'Hello, Python!   ' — left only
print(raw.rstrip())       # '   Hello, Python!' — right only

# strip specific characters
print("###title###".strip("#"))   # 'title'
print("***data***".strip("*"))    # 'data'

# ── replace — substitute substrings ───────────────────────────
text = "I luv Python. Python luv me."
fixed = text.replace("luv", "love")
print(fixed)
# 'I love Python. Python love me.'

# replace with count limit — only first N occurrences
once = text.replace("luv", "love", 1)
print(once)
# 'I love Python. Python luv me.'

# remove all spaces
no_spaces = "hello world".replace(" ", "")
print(no_spaces)   # 'helloworld'

# ── find — locate first occurrence; returns index or -1 ───────
s = "Python is fun and Python is powerful"

idx = s.find("Python")       # 0  — first match index
idx2 = s.find("Python", 5)   # 17 — search from index 5
idx3 = s.find("Java")        # -1 — not found, no crash

# rfind — search from the right
last = s.rfind("Python")     # 17

print(idx, idx2, idx3, last)
# 0 17 -1 17

# ── Use 'in' for simple existence checks ──────────────────────
print("Python" in s)    # True
print("Java" in s)      # False

# ── Other essential methods ────────────────────────────────────
text = "Hello, World!"

print(text.upper())              # 'HELLO, WORLD!'
print(text.lower())              # 'hello, world!'
print(text.title())              # 'Hello, World!'
print(text.startswith("Hello"))  # True
print(text.endswith("!"))        # True
print(text.count("l"))           # 3
print(text.isdigit())            # False
print("12345".isdigit())         # True
print("Python3".isalnum())       # True
```

---

## Step 2: String Slicing Mastery

Slicing syntax: `s[start:stop:step]`  
- `start` — index to begin (inclusive), default `0`
- `stop`  — index to end (exclusive), default `len(s)`
- `step`  — how many chars to skip, default `1`

```
s = "P y t h o n 3 . 1 1"
     0 1 2 3 4 5 6 7 8 9    ← positive
    -10-9-8-7-6-5-4-3-2-1   ← negative
```

```python
s = "Python3.11"

# ── Basic slicing ──────────────────────────────────────────────
print(s[0:6])       # 'Python'   — chars 0 to 5
print(s[6:])        # '3.11'     — from index 6 to end
print(s[:6])        # 'Python'   — from start to index 5
print(s[0:10])      # 'Python3.11' — full string

# ── Negative indexing ─────────────────────────────────────────
print(s[-4:])       # '.11'      — last 4 chars
print(s[-4:-1])     # '.1'       — negative range
print(s[-1])        # '1'        — last char

# ── Step slicing ──────────────────────────────────────────────
print(s[::2])       # 'Pto.1'    — every 2nd char
print(s[1::2])      # 'yhn31'    — every 2nd, starting at 1
print(s[::-1])      # '11.3nohtyP' — REVERSE the string ← classic trick

# ── Practical slicing examples ────────────────────────────────
url      = "https://python.org/docs"
protocol = url[:5]              # 'https'
domain   = url[8:18]            # 'python.org'

filename = "report_2024.csv"
ext      = filename[-3:]        # 'csv'
name     = filename[:-4]        # 'report_2024'

email    = "alice@example.com"
user     = email[:email.find("@")]    # 'alice'
domain   = email[email.find("@")+1:]  # 'example.com'

# ── Slicing never raises IndexError ───────────────────────────
print("Hi"[0:100])    # 'Hi' — safe, no error
print("Hi"[5:])       # ''   — empty string, no crash

# ── String is immutable — slicing returns NEW string ─────────
s = "Python"
s[:3]         # 'Pyt'  — original s unchanged
new = s[:3] + "3"   # 'Pyt3'  — build a new string

# ── Palindrome check using reverse slice ─────────────────────
def is_palindrome(word: str) -> bool:
    w = word.lower().replace(" ", "")
    return w == w[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("madam"))    # True
print(is_palindrome("Python"))   # False
```

---

## Step 3: Regular Expressions — `re` module

Regular expressions (regex) are **patterns** for matching, extracting, and replacing text. Essential for NLP, log parsing, data cleaning, and form validation.

**The 4 most used functions:**

| Function | What it does |
|---|---|
| `re.search(pattern, text)` | Find FIRST match anywhere → match object or `None` |
| `re.findall(pattern, text)` | Find ALL matches → list of strings |
| `re.sub(pattern, repl, text)` | Replace matches → new string |
| `re.match(pattern, text)` | Match only at START of string |

```python
import re

text = "Call +91-9876543210 or email support@python.org by 2024-12-31"

# ── re.search — find first match ──────────────────────────────
match = re.search(r'\d{4}-\d{2}-\d{2}', text)
if match:
    print(match.group())     # '2024-12-31'
    print(match.start())     # 45  — index where match begins
    print(match.end())       # 55  — index where match ends

# ── re.findall — find all matches → list ──────────────────────
digits  = re.findall(r'\d+', text)
print(digits)
# ['91', '9876543210', '2024', '12', '31']

emails  = re.findall(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b', text)
print(emails)
# ['support@python.org']

phones  = re.findall(r'\+?\d[\d\-]{8,12}\d', text)
print(phones)
# ['+91-9876543210']

# ── re.sub — find and replace with pattern ────────────────────
clean   = re.sub(r'\d+', 'NUM', "Price: 500 and Qty: 10")
print(clean)
# 'Price: NUM and Qty: NUM'

# Remove all punctuation
no_punct = re.sub(r'[^\w\s]', '', "Hello, World! How's Python?")
print(no_punct)
# 'Hello World Hows Python'

# Collapse multiple spaces into one
neat = re.sub(r'\s+', ' ', "Python   is    great")
print(neat.strip())
# 'Python is great'

# ── re.match — only matches at start ──────────────────────────
m1 = re.match(r'Call', text)     # match object — 'Call' is at start
m2 = re.match(r'email', text)    # None — 'email' is not at start

# ── re.split — split on a pattern ────────────────────────────
parts = re.split(r'[.!?]+', "Hello! How are you? Fine.")
print(parts)
# ['Hello', ' How are you', ' Fine', '']

sentences = [s.strip() for s in parts if s.strip()]
print(sentences)
# ['Hello', 'How are you', 'Fine']
```

**Key regex patterns cheat-sheet:**

| Pattern | Matches |
|---|---|
| `\d` | Any digit `[0-9]` |
| `\D` | Any non-digit |
| `\w` | Word char `[a-zA-Z0-9_]` |
| `\W` | Non-word char |
| `\s` | Whitespace (space, tab, newline) |
| `\S` | Non-whitespace |
| `.` | Any char except newline |
| `+` | 1 or more of previous |
| `*` | 0 or more of previous |
| `?` | 0 or 1 of previous |
| `{n}` | Exactly n repetitions |
| `{n,m}` | Between n and m repetitions |
| `^` | Start of string |
| `$` | End of string |
| `[abc]` | Any of a, b, or c |
| `[^abc]` | Any char NOT a, b, or c |
| `\b` | Word boundary |
| `.*?` | Non-greedy: match as little as possible |

```python
import re

# ── Compile for reuse (faster in loops) ───────────────────────
email_pattern = re.compile(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b')

texts = [
    "Email me at alice@example.com",
    "No email here",
    "bob@test.org is the address"
]
for t in texts:
    found = email_pattern.findall(t)
    if found:
        print(found)
# ['alice@example.com']
# ['bob@test.org']

# ── Groups — extract parts of a match ────────────────────────
log = "2024-12-31 ERROR: Connection timeout"
m = re.search(r'(\d{4}-\d{2}-\d{2})\s+(ERROR|INFO|WARN):\s+(.+)', log)
if m:
    date, level, message = m.groups()
    print(f"Date: {date}, Level: {level}, Msg: {message}")
# Date: 2024-12-31, Level: ERROR, Msg: Connection timeout
```

---

## Step 4: Format Strings for Output

Python has three formatting approaches — **f-strings are the modern standard**.

```python
name  = "Alice"
score = 95.6789
rank  = 1
budget = 1500000

# ── 1. f-strings (Python 3.6+) — USE THESE ───────────────────
print(f"Name: {name}, Score: {score:.2f}, Rank: #{rank}")
# Name: Alice, Score: 95.68, Rank: #1

# ── Alignment and padding ─────────────────────────────────────
# < left-align   > right-align   ^ center-align
header = f"{'Name':<12} {'Score':>8} {'Grade':^6}"
row    = f"{name:<12} {score:>8.2f} {'A+':^6}"
print(header)
print(row)
# Name           Score  Grade
# Alice           95.68   A+

# ── Number formatting ─────────────────────────────────────────
print(f"Budget : ₹{budget:,.0f}")    # ₹1,500,000  — thousand separator
print(f"Score  : {score:.4f}")       # 95.6789     — 4 decimal places
print(f"Score  : {score:.0f}")       # 96           — rounded to int
print(f"Percent: {0.9567:.1%}")      # 95.7%        — auto percentage
print(f"Sci    : {0.000123:.2e}")    # 1.23e-04     — scientific notation
print(f"Hex    : {255:#x}")          # 0xff         — hex with prefix
print(f"Binary : {10:#b}")           # 0b1010       — binary with prefix

# ── Expressions inside f-strings ─────────────────────────────
items = ["apple", "banana", "cherry"]
print(f"Items: {', '.join(items)}")             # Items: apple, banana, cherry
print(f"Upper: {name.upper()}")                 # Upper: ALICE
print(f"Score > 90? {score > 90}")              # Score > 90? True

# ── Multi-line f-string ───────────────────────────────────────
report = (
    f"{'=' * 30}\n"
    f"  Student: {name}\n"
    f"  Score  : {score:.2f}\n"
    f"  Rank   : #{rank}\n"
    f"{'=' * 30}"
)
print(report)

# ── 2. .format() — useful for reusable templates ──────────────
template = "Dear {name}, your score is {score:.1f} — {grade}."
print(template.format(name="Bob", score=88.5, grade="B+"))

# Positional
print("Hello {} from {}!".format("Alice", "Chennai"))

# ── 3. % formatting — legacy, avoid in new code ───────────────
print("Hello %s, score: %.2f" % (name, score))
```

---

## Step 5: Nested String Operations

```python
# ── Chaining methods ──────────────────────────────────────────
raw = "  HELLO, World! This is Python.  "
clean = raw.strip().lower().replace(",", "").replace(".", "")
print(clean)
# 'hello world! this is python'

# ── Tokenization (NLP preprocessing step) ─────────────────────
import re

def tokenize(text: str) -> list:
    """Simple tokenizer: lowercase, strip punctuation, split."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)   # remove punctuation
    text = re.sub(r'\s+', ' ', text)       # normalize whitespace
    return text.strip().split()

tokens = tokenize("Hello! This is Python 3.11 — amazing stuff.")
print(tokens)
# ['hello', 'this', 'is', 'python', '311', 'amazing', 'stuff']

# ── Multiline strings ─────────────────────────────────────────
text = """Line 1: Python basics
Line 2: String methods
Line 3: Regular expressions"""

lines = text.strip().split("\n")
for i, line in enumerate(lines, 1):
    print(f"{i}. {line.split(': ')[1]}")
# 1. Python basics
# 2. String methods
# 3. Regular expressions

# ── String joining patterns ───────────────────────────────────
# Build CSV row
fields = ["Alice", "25", "Chennai", "Developer"]
csv_row = ",".join(fields)
print(csv_row)   # Alice,25,Chennai,Developer

# Build HTML list
items = ["Python", "FastAPI", "LangChain"]
html  = "<ul>\n" + "".join(f"  <li>{i}</li>\n" for i in items) + "</ul>"
print(html)
```

---

## Practice Project — Text Analyzer Tool

Create `text_analyzer.py`:

```python
# text_analyzer.py — Day 6 project
import re
from collections import Counter

def analyze_text(text: str) -> dict:
    """
    Analyze input text and return comprehensive statistics.
    Mimics real NLP pre-processing used in AI/ML pipelines.

    Args:
        text: Raw input string to analyze.

    Returns:
        dict with counts, vocabulary stats, and extracted entities.
    """
    # ── Cleaning ──────────────────────────────────────────────
    cleaned  = text.strip()
    lower    = cleaned.lower()

    # ── Counts ────────────────────────────────────────────────
    char_count      = len(cleaned)
    char_no_spaces  = len(cleaned.replace(" ", ""))
    words           = lower.split()
    word_count      = len(words)
    sentences       = [s.strip() for s in re.split(r'[.!?]+', cleaned) if s.strip()]
    sentence_count  = len(sentences)
    paragraphs      = [p.strip() for p in cleaned.split("\n\n") if p.strip()]

    # ── Vocabulary ────────────────────────────────────────────
    clean_words = [re.sub(r'[^a-z]', '', w) for w in words]
    clean_words = [w for w in clean_words if w]
    word_freq   = Counter(clean_words)
    top_5       = word_freq.most_common(5)

    # ── Averages ──────────────────────────────────────────────
    avg_word_len      = sum(len(w) for w in clean_words) / max(word_count, 1)
    avg_sentence_len  = word_count / max(sentence_count, 1)
    unique_word_ratio = len(word_freq) / max(word_count, 1)

    # ── Pattern extraction ────────────────────────────────────
    emails = re.findall(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b', cleaned)
    urls   = re.findall(r'https?://\S+', cleaned)
    dates  = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', cleaned)
    phones = re.findall(r'\+?\d[\d\-]{8,12}\d', cleaned)

    # ── Sentence classification ───────────────────────────────
    questions    = [s for s in sentences if cleaned.find(s) >= 0
                    and cleaned[cleaned.find(s) + len(s):cleaned.find(s) + len(s) + 1] == "?"]
    exclamations = [s for s in sentences
                    if re.search(re.escape(s) + r'\s*!', cleaned)]

    return {
        "char_count"          : char_count,
        "char_no_spaces"      : char_no_spaces,
        "word_count"          : word_count,
        "sentence_count"      : sentence_count,
        "paragraph_count"     : len(paragraphs),
        "unique_words"        : len(word_freq),
        "unique_word_ratio"   : f"{unique_word_ratio:.2%}",
        "avg_word_length"     : f"{avg_word_len:.2f} chars",
        "avg_sentence_length" : f"{avg_sentence_len:.1f} words",
        "top_5_words"         : top_5,
        "emails_found"        : emails,
        "urls_found"          : urls,
        "dates_found"         : dates,
        "phones_found"        : phones,
    }


def print_report(result: dict) -> None:
    """Pretty-print the analysis report using f-string formatting."""
    print("=" * 52)
    print(f"{'📊  TEXT ANALYSIS REPORT':^52}")
    print("=" * 52)

    sections = {
        "📏  Counts": [
            "char_count", "char_no_spaces", "word_count",
            "sentence_count", "paragraph_count"
        ],
        "🔠  Vocabulary": [
            "unique_words", "unique_word_ratio",
            "avg_word_length", "avg_sentence_length"
        ],
        "🏆  Top 5 Words"   : ["top_5_words"],
        "🔍  Extracted Data": ["emails_found", "urls_found",
                                "dates_found",  "phones_found"],
    }

    for section, keys in sections.items():
        print(f"\n{section}")
        print("-" * 30)
        for key in keys:
            label = key.replace("_", " ").title()
            value = result[key]
            if isinstance(value, list) and value and isinstance(value[0], tuple):
                print(f"  {label}:")
                for word, count in value:
                    bar = "█" * count
                    print(f"    {word:<15} {count:>2}x  {bar}")
            elif isinstance(value, list):
                if value:
                    for item in value:
                        print(f"  {label:<22}: {item}")
                else:
                    print(f"  {label:<22}: (none found)")
            else:
                print(f"  {label:<22}: {value}")

    print("\n" + "=" * 52)


# ── Main ──────────────────────────────────────────────────────
if __name__ == "__main__":
    sample = """
    Python is an amazing programming language. Python is used in AI, ML,
    web development, and data science. Many developers love Python because
    Python is easy to learn and very powerful.

    Contact us at support@python.org or visit https://python.org for docs.
    Release date: 2024-10-07. Call: +91-9876543210.
    Python, python, PYTHON — all count as the same word after lowercasing!
    """

    result = analyze_text(sample)
    print_report(result)

    # ── Bonus: Interactive mode ────────────────────────────────
    print("\n" + "=" * 52)
    print("📝  INTERACTIVE MODE — paste your own text")
    print("    (type 'quit' on a new line and press Enter twice to finish)")
    print("=" * 52)
    lines = []
    try:
        while True:
            line = input()
            if line.strip().lower() == "quit":
                break
            lines.append(line)
        if lines:
            user_text = "\n".join(lines)
            print_report(analyze_text(user_text))
    except EOFError:
        pass
```

**Expected output:**

```
====================================================
              📊  TEXT ANALYSIS REPORT
====================================================

📏  Counts
------------------------------
  Char Count             : 382
  Char No Spaces         : 304
  Word Count             : 65
  Sentence Count         : 5
  Paragraph Count        : 2

🔠  Vocabulary
------------------------------
  Unique Words           : 39
  Unique Word Ratio      : 60.00%
  Avg Word Length        : 6.12 chars
  Avg Sentence Length    : 13.0 words

🏆  Top 5 Words
------------------------------
  python          6x  ██████
  is              4x  ████
  and             3x  ███
  very            1x  █
  amazing         1x  █

🔍  Extracted Data
------------------------------
  Emails Found           : support@python.org
  Urls Found             : https://python.org
  Dates Found            : 2024-10-07
  Phones Found           : +91-9876543210
```

---

## 🚀 Bonus Challenges

```python
import re

# 1. Caesar cipher — shift each letter by N positions
def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

print(caesar_cipher("Hello, Python!", 3))   # 'Khoor, Sbwkrq!'
print(caesar_cipher("Khoor, Sbwkrq!", -3))  # 'Hello, Python!'

# 2. Extract all hashtags from social media text
tweet = "Loving #Python and #AI! Check out #MachineLearning today."
tags  = re.findall(r'#\w+', tweet)
print(tags)   # ['#Python', '#AI', '#MachineLearning']

# 3. Validate Indian mobile numbers
def is_valid_indian_mobile(number: str) -> bool:
    pattern = r'^(\+91|91|0)?[6-9]\d{9}$'
    return bool(re.match(pattern, number.replace("-", "").replace(" ", "")))

print(is_valid_indian_mobile("+91-9876543210"))  # True
print(is_valid_indian_mobile("9123456789"))       # True
print(is_valid_indian_mobile("1234567890"))       # False

# 4. Title-case every word except articles/prepositions
def smart_title(text: str) -> str:
    minor = {"a", "an", "the", "and", "but", "or", "in", "on", "at", "of"}
    words = text.lower().split()
    titled = [w.title() if i == 0 or w not in minor else w
              for i, w in enumerate(words)]
    return " ".join(titled)

print(smart_title("the art of war in the modern age"))
# 'The Art of War in the Modern Age'

# 5. Count vowels, consonants, digits, spaces
def char_stats(text: str) -> dict:
    return {
        "vowels"     : len(re.findall(r'[aeiouAEIOU]', text)),
        "consonants" : len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text)),
        "digits"     : len(re.findall(r'\d', text)),
        "spaces"     : text.count(" "),
    }

print(char_stats("Hello Python3"))
# {'vowels': 4, 'consonants': 7, 'digits': 1, 'spaces': 1}
```

---

## 📋 Day 6 Summary

| Concept | Syntax | Notes |
|---|---|---|
| Split by delimiter | `s.split(",")` | Returns list |
| Split on whitespace | `s.split()` | Default — any whitespace |
| Join list to string | `",".join(lst)` | Separator first |
| Strip whitespace | `s.strip()` | Both sides; `.lstrip()` / `.rstrip()` for one side |
| Strip specific chars | `s.strip("#")` | Removes given chars |
| Replace substring | `s.replace("a", "b")` | Returns new string |
| Find index | `s.find("x")` | Returns -1 if not found |
| Check existence | `"x" in s` | Returns True/False |
| Basic slicing | `s[start:stop]` | stop is exclusive |
| Step slicing | `s[::2]` | Every 2nd char |
| Reverse string | `s[::-1]` | Classic Python trick |
| Negative index | `s[-1]` | Last char; `s[-3:]` last 3 |
| Find first match | `re.search(pat, s)` | Returns match object or None |
| Find all matches | `re.findall(pat, s)` | Returns list of strings |
| Replace by pattern | `re.sub(pat, repl, s)` | Returns new string |
| Match at start | `re.match(pat, s)` | Only checks beginning |
| Split by pattern | `re.split(pat, s)` | Returns list |
| f-string | `f"{var:.2f}"` | Preferred formatting |
| Align/pad | `f"{val:<10}"` | `<` left `>` right `^` center |
| Thousand separator | `f"{n:,}"` | `1000` → `1,000` |
| Percentage format | `f"{0.956:.1%}"` | `95.6%` |
| Compile regex | `re.compile(pattern)` | Reuse pattern in loops |
| Regex group | `m.group(1)` | Extract sub-pattern |

---

## 📚 Resources

- [Real Python — Python Strings](https://realpython.com/python-strings/)
- [Python Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Real Python — Regular Expressions](https://realpython.com/regex-python/)
- [Regex101 — Interactive Tester](https://regex101.com/)
- [Python Docs — re module](https://docs.python.org/3/library/re.html)

---

## ➡️ What's Next — Day 7

Tomorrow: **File Handling** — reading, writing, and managing files with Python.

```python
# Preview of Day 7
with open("data.txt", "w") as f:
    f.write("Hello, File World!\n")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)     # 'Hello, File World!'

# Reading CSV manually
with open("students.csv", "r") as f:
    for line in f:
        fields = line.strip().split(",")
        print(fields)
```

Keep going — strings and regex are the foundation of every data cleaning step, log parser, and NLP pipeline you'll build with Python. 🚀
