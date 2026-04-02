# 🐍 Python Day 7 — File Handling: Read & Write Files

> **Phase 1 · Week 1 · Day 7** | Beginner → Job-Ready Python for AI & ML

---

## 📋 What You'll Learn Today

- `open()`, `read()`, `write()`, `close()` — the basics of file I/O
- `with` statement (context manager) — the right way to handle files
- Read/write CSV files manually — without any library
- `os` module — file system operations, paths, environment
- `pathlib` module — modern object-oriented path handling
- **Practice Project:** Log file parser

---

## The Mental Model

Files are **persistent storage** — data survives after the program ends. Python uses a simple open → do work → close pattern. The `with` statement automates the close step so you never leak file handles, even when errors occur.

```
Program Memory          Disk / File System
┌─────────────┐         ┌──────────────────┐
│  variables  │  open() │   data.txt       │
│  lists      │ ───────►│   students.csv   │
│  dicts      │ read()  │   app.log        │
│             │◄─────── │   config.json    │
└─────────────┘ write() └──────────────────┘
                close()
```

---

## Step 1: open(), read(), write(), close()

Create `day7.py` and type this:

```python
# ── Writing a file ────────────────────────────────────────────
# open(filename, mode)
# Modes: 'r' read  'w' write (overwrites)  'a' append  'x' create new
#        'b' binary  't' text (default)   '+' read+write

f = open("hello.txt", "w")       # open for writing — creates if not exists
f.write("Hello, File World!\n")  # write a string; \n = newline
f.write("Python file I/O is easy.\n")
f.close()                         # ALWAYS close — flushes buffer to disk

# ── Reading a file — read() ────────────────────────────────────
f = open("hello.txt", "r")       # open for reading (default mode)
content = f.read()                # read entire file as one string
print(content)
# Hello, File World!
# Python file I/O is easy.
f.close()

# ── Reading line by line — readline() ─────────────────────────
f = open("hello.txt", "r")
line1 = f.readline()              # read one line including \n
line2 = f.readline()
print(repr(line1))                # 'Hello, File World!\n'
print(repr(line2))                # 'Python file I/O is easy.\n'
f.close()

# ── Reading all lines — readlines() ───────────────────────────
f = open("hello.txt", "r")
lines = f.readlines()             # returns list of strings
print(lines)
# ['Hello, File World!\n', 'Python file I/O is easy.\n']
f.close()

# ── Appending to a file ───────────────────────────────────────
f = open("hello.txt", "a")       # 'a' appends — does NOT overwrite
f.write("Line 3 appended.\n")
f.close()

# ── Writing multiple lines at once ────────────────────────────
lines_to_write = ["Alpha\n", "Beta\n", "Gamma\n"]
f = open("letters.txt", "w")
f.writelines(lines_to_write)      # write list of strings (no auto \n)
f.close()

# ── File modes summary ────────────────────────────────────────
# 'r'  — read only          (file must exist)
# 'w'  — write only         (creates new OR overwrites existing)
# 'a'  — append             (creates new OR adds to end)
# 'x'  — exclusive create   (fails if file already exists)
# 'r+' — read AND write     (file must exist, no truncation)
# 'rb' — read binary        (images, PDFs, etc.)
# 'wb' — write binary
```

---

## Step 2: with Statement — Context Manager

The `with` statement **automatically closes the file** when the block exits — even if an exception occurs. Always use `with` in real code.

```python
# ── Writing with 'with' ───────────────────────────────────────
with open("notes.txt", "w") as f:
    f.write("Context managers are great.\n")
    f.write("No need to call f.close()!\n")
# file is automatically closed here — even if an error occurs inside

# ── Reading with 'with' ───────────────────────────────────────
with open("notes.txt", "r") as f:
    content = f.read()
print(content)

# ── Iterating line by line — most memory-efficient ────────────
with open("notes.txt", "r") as f:
    for line in f:                       # file object is iterable
        print(line.strip())              # strip() removes trailing \n

# ── Reading into a clean list ─────────────────────────────────
with open("notes.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]
print(lines)
# ['Context managers are great.', 'No need to call f.close()!']

# ── Writing multiple lines cleanly ────────────────────────────
students = ["Alice", "Bob", "Carol", "Dave"]
with open("students.txt", "w") as f:
    for name in students:
        f.write(f"{name}\n")

# ── Appending with 'with' ─────────────────────────────────────
with open("students.txt", "a") as f:
    f.write("Eve\n")
    f.write("Frank\n")

# ── Read and write at the same time ──────────────────────────
with open("notes.txt", "r+") as f:
    content = f.read()
    f.seek(0)                            # move cursor back to start
    f.write(content.upper())             # overwrite with uppercased text

# ── encoding — always specify for non-ASCII text ──────────────
with open("tamil.txt", "w", encoding="utf-8") as f:
    f.write("வணக்கம் Python!\n")        # Tamil + English

with open("tamil.txt", "r", encoding="utf-8") as f:
    print(f.read())                      # வணக்கம் Python!

# ── Why 'with' beats manual open/close ───────────────────────
# Manual — risky:
f = open("data.txt", "r")
# ... if an exception happens here, f.close() never runs → file leak
f.close()

# With — safe:
with open("data.txt", "r") as f:
    pass                                 # file always closed — no leak
```

---

## Step 3: Read/Write CSV Files Manually

CSV (Comma-Separated Values) is the most common data format in data science and AI. Here we handle it **without any library** — understanding the format deeply.

```python
# ── Writing a CSV manually ────────────────────────────────────
headers = ["id", "name", "age", "score", "city"]
rows = [
    ["1", "Alice",  "25", "92.5", "Chennai"],
    ["2", "Bob",    "28", "78.0", "Mumbai"],
    ["3", "Carol",  "23", "96.0", "Chennai"],
    ["4", "Dave",   "30", "65.5", "Delhi"],
    ["5", "Eve",    "26", "88.0", "Bangalore"],
]

with open("students.csv", "w", encoding="utf-8") as f:
    f.write(",".join(headers) + "\n")    # header row
    for row in rows:
        f.write(",".join(row) + "\n")    # data rows

# ── Reading a CSV manually ────────────────────────────────────
with open("students.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")
print("Columns:", header)
# Columns: ['id', 'name', 'age', 'score', 'city']

data = []
for line in lines[1:]:                   # skip header row
    fields = line.strip().split(",")
    data.append(fields)

for row in data:
    print(row)
# ['1', 'Alice', '25', '92.5', 'Chennai']
# ['2', 'Bob',   '28', '78.0', 'Mumbai']

# ── Parse CSV into list of dicts ──────────────────────────────
with open("students.csv", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

keys = lines[0].split(",")
records = [dict(zip(keys, line.split(","))) for line in lines[1:]]

for r in records:
    print(f"{r['name']:<8} | score: {float(r['score']):.1f} | {r['city']}")
# Alice    | score: 92.5 | Chennai
# Bob      | score: 78.0 | Mumbai

# ── Filter and analyse ────────────────────────────────────────
chennai_students = [r for r in records if r["city"] == "Chennai"]
scores           = [float(r["score"]) for r in records]
avg_score        = sum(scores) / len(scores)
top_student      = max(records, key=lambda r: float(r["score"]))

print(f"Chennai students : {len(chennai_students)}")
print(f"Average score    : {avg_score:.2f}")
print(f"Top student      : {top_student['name']} ({top_student['score']})")

# ── Write filtered results to a new CSV ───────────────────────
high_scorers = [r for r in records if float(r["score"]) >= 85]

with open("high_scorers.csv", "w", encoding="utf-8") as f:
    f.write(",".join(keys) + "\n")
    for r in high_scorers:
        f.write(",".join(r[k] for k in keys) + "\n")

print("high_scorers.csv written!")

# ── Handle CSV with commas in values — quote fields ──────────
import csv   # stdlib csv module — handles edge cases properly

with open("safe.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "note"])
    writer.writerow(["Alice", "Loves Python, FastAPI"])   # comma in value — handled!
    writer.writerow(["Bob",   'He said "great"'])          # quotes — handled!

with open("safe.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# {'name': 'Alice', 'note': 'Loves Python, FastAPI'}
# {'name': 'Bob',   'note': 'He said "great"'}
```

---

## Step 4: os Module — File System Operations

The `os` module lets you interact with the operating system: navigate directories, check paths, rename/delete files, and read environment variables.

```python
import os

# ── Current working directory ─────────────────────────────────
cwd = os.getcwd()
print(cwd)                           # /home/user/Python  (or C:\Users\...)

# ── List directory contents ───────────────────────────────────
entries = os.listdir(".")            # list current dir
print(entries)                       # ['day7.py', 'students.csv', ...]

# ── Check existence ───────────────────────────────────────────
print(os.path.exists("students.csv"))   # True / False
print(os.path.isfile("students.csv"))   # True — it's a file
print(os.path.isdir("Day7"))            # True — it's a directory

# ── Path operations ───────────────────────────────────────────
full_path = os.path.abspath("students.csv")
print(full_path)   # /home/user/Python/students.csv

dirname  = os.path.dirname(full_path)   # /home/user/Python
basename = os.path.basename(full_path)  # students.csv
name, ext = os.path.splitext(basename)  # ('students', '.csv')

# Join paths safely (handles / vs \ automatically)
log_path = os.path.join(cwd, "logs", "app.log")
print(log_path)    # /home/user/Python/logs/app.log

# ── Create directories ────────────────────────────────────────
os.makedirs("logs", exist_ok=True)          # create; ok if already exists
os.makedirs("data/processed", exist_ok=True) # create nested dirs

# ── File info — size, timestamps ──────────────────────────────
if os.path.exists("students.csv"):
    size  = os.path.getsize("students.csv")  # bytes
    mtime = os.path.getmtime("students.csv") # last modified (timestamp)
    print(f"Size: {size} bytes")

# ── Rename and remove ─────────────────────────────────────────
# os.rename("old.txt", "new.txt")   # rename or move
# os.remove("temp.txt")             # delete file (no recycle bin!)
# os.rmdir("empty_dir")             # delete EMPTY directory only

# ── Walk directory tree ───────────────────────────────────────
for root, dirs, files in os.walk("."):
    level = root.replace(".", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")
    for file in files:
        print(f"{indent}  {file}")

# ── Environment variables ─────────────────────────────────────
home = os.environ.get("HOME", "unknown")   # safe read with default
path = os.environ.get("PATH", "")
print(f"Home: {home}")

# Set env var (affects current process only)
os.environ["MY_APP_DEBUG"] = "true"
print(os.environ.get("MY_APP_DEBUG"))      # 'true'
```

---

## Step 5: pathlib Module — Modern Path Handling

`pathlib` (Python 3.4+) treats paths as **objects** instead of strings. It's more readable, cross-platform, and the modern standard for file path work.

```python
from pathlib import Path

# ── Creating Path objects ─────────────────────────────────────
p = Path(".")                        # current directory
home = Path.home()                   # home directory
print(home)                          # /home/user  or  C:\Users\user

# ── Building paths with / operator ───────────────────────────
data_dir  = Path(".") / "data"
csv_file  = data_dir / "students.csv"
log_file  = Path(".") / "logs" / "app.log"

print(csv_file)                      # data/students.csv
print(csv_file.resolve())            # /home/user/Python/data/students.csv

# ── Path properties ───────────────────────────────────────────
p = Path("data/students.csv")
print(p.name)        # 'students.csv'     — filename with extension
print(p.stem)        # 'students'         — filename without extension
print(p.suffix)      # '.csv'             — just the extension
print(p.suffixes)    # ['.csv']           — list (e.g. ['.tar', '.gz'])
print(p.parent)      # data               — parent directory
print(p.parts)       # ('data', 'students.csv')

# ── Check / create ────────────────────────────────────────────
csv_path = Path("students.csv")
print(csv_path.exists())             # True / False
print(csv_path.is_file())            # True
print(csv_path.is_dir())             # False

Path("logs").mkdir(parents=True, exist_ok=True)    # create directory

# ── Read and write with pathlib ───────────────────────────────
# Write text
Path("hello.txt").write_text("Hello from pathlib!\n", encoding="utf-8")

# Read text
content = Path("hello.txt").read_text(encoding="utf-8")
print(content)                       # Hello from pathlib!

# Write bytes (binary)
Path("data.bin").write_bytes(b"\x00\x01\x02\x03")

# Read bytes
raw = Path("data.bin").read_bytes()
print(raw)                           # b'\x00\x01\x02\x03'

# ── List and glob ─────────────────────────────────────────────
# List all files in directory
for f in Path(".").iterdir():
    if f.is_file():
        print(f.name)

# Glob — find files matching a pattern
csv_files = list(Path(".").glob("*.csv"))
print(csv_files)      # [PosixPath('students.csv'), PosixPath('high_scorers.csv')]

# Recursive glob — search subdirectories
all_py = list(Path(".").rglob("*.py"))
print(all_py)         # all .py files in current dir and subdirs

# ── File stats ────────────────────────────────────────────────
stat = csv_path.stat()
print(f"Size  : {stat.st_size} bytes")
print(f"Mtime : {stat.st_mtime}")

# ── Rename and unlink (delete) ────────────────────────────────
# Path("old.txt").rename(Path("new.txt"))     # rename
# Path("temp.txt").unlink(missing_ok=True)    # delete (safe if missing)
# Path("empty_dir").rmdir()                   # delete empty dir

# ── os vs pathlib quick comparison ───────────────────────────
import os
# os style:
os.path.join("data", "students.csv")         # 'data/students.csv'
os.path.exists("students.csv")               # True/False
os.path.splitext("students.csv")[1]          # '.csv'

# pathlib style (cleaner):
(Path("data") / "students.csv")              # data/students.csv
Path("students.csv").exists()                # True/False
Path("students.csv").suffix                  # '.csv'
```

---

## Practice Project — Log File Parser

Create `log_parser.py`:

```python
# log_parser.py — Day 7 project
import re
from pathlib import Path
from collections import Counter
from datetime import datetime


# ── Step 1: Generate a sample log file ───────────────────────
def create_sample_log(path: str = "app.log") -> None:
    """Write a realistic app log file for parsing."""
    log_lines = [
        "2024-12-01 08:00:01 INFO  Server started on port 8000",
        "2024-12-01 08:01:15 INFO  User alice@example.com logged in",
        "2024-12-01 08:03:22 WARNING  High memory usage: 82%",
        "2024-12-01 08:05:10 INFO  User bob@test.org logged in",
        "2024-12-01 08:07:45 ERROR  Database connection timeout after 30s",
        "2024-12-01 08:09:00 INFO  User carol@company.com logged in",
        "2024-12-01 08:10:33 ERROR  FileNotFoundError: config.yaml not found",
        "2024-12-01 08:12:01 WARNING  API rate limit at 90%",
        "2024-12-01 08:14:55 INFO  Scheduled backup completed successfully",
        "2024-12-01 08:16:20 ERROR  ConnectionRefusedError: Redis unreachable",
        "2024-12-01 08:18:00 INFO  User dave@example.com logged in",
        "2024-12-01 08:20:11 WARNING  Slow query detected: 4.2s",
        "2024-12-01 08:22:30 INFO  Cache cleared",
        "2024-12-01 08:25:00 ERROR  Timeout: external API did not respond",
        "2024-12-01 08:27:45 INFO  User eve@test.org logged in",
        "2024-12-01 08:30:00 INFO  Health check passed",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"✅ Sample log written → {path}")


# ── Step 2: Parse each log line into a dict ───────────────────
def parse_log_line(line: str) -> dict | None:
    """
    Parse a log line into structured data.

    Expected format:
        YYYY-MM-DD HH:MM:SS LEVEL  Message

    Returns:
        dict with keys: date, time, datetime, level, message
        None if line does not match the expected format.
    """
    pattern = r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR|DEBUG)\s+(.+)$'
    match = re.match(pattern, line.strip())
    if not match:
        return None
    date_str, time_str, level, message = match.groups()
    return {
        "date"    : date_str,
        "time"    : time_str,
        "datetime": datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S"),
        "level"   : level,
        "message" : message,
    }


# ── Step 3: Load and parse the entire log file ────────────────
def load_log(path: str) -> list[dict]:
    """Read log file and return list of parsed entry dicts."""
    log_path = Path(path)
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    entries = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            parsed = parse_log_line(line)
            if parsed:
                parsed["line_num"] = line_num
                entries.append(parsed)
            else:
                if line.strip():    # ignore blank lines silently
                    print(f"  ⚠️  Line {line_num} skipped (unrecognised format): {line.strip()[:60]}")
    return entries


# ── Step 4: Analyse the parsed entries ───────────────────────
def analyse_log(entries: list[dict]) -> dict:
    """Return summary statistics from parsed log entries."""
    if not entries:
        return {}

    level_counts = Counter(e["level"] for e in entries)
    errors       = [e for e in entries if e["level"] == "ERROR"]
    warnings     = [e for e in entries if e["level"] == "WARNING"]
    emails       = []
    for e in entries:
        found = re.findall(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b', e["message"])
        emails.extend(found)

    start = min(e["datetime"] for e in entries)
    end   = max(e["datetime"] for e in entries)

    return {
        "total_entries" : len(entries),
        "level_counts"  : dict(level_counts),
        "error_count"   : level_counts.get("ERROR", 0),
        "warning_count" : level_counts.get("WARNING", 0),
        "info_count"    : level_counts.get("INFO", 0),
        "errors"        : errors,
        "warnings"      : warnings,
        "unique_users"  : list(set(emails)),
        "time_range"    : (start.strftime("%H:%M:%S"), end.strftime("%H:%M:%S")),
        "duration_mins" : round((end - start).seconds / 60, 1),
    }


# ── Step 5: Print a formatted report ─────────────────────────
def print_report(stats: dict) -> None:
    """Pretty-print the log analysis report."""
    print("\n" + "=" * 56)
    print(f"{'📋  LOG FILE ANALYSIS REPORT':^56}")
    print("=" * 56)

    print(f"\n{'📊  Overview'}")
    print("-" * 30)
    print(f"  {'Total entries':<22}: {stats['total_entries']}")
    print(f"  {'Time range':<22}: {stats['time_range'][0]} → {stats['time_range'][1]}")
    print(f"  {'Duration':<22}: {stats['duration_mins']} minutes")

    print(f"\n{'📈  Log Levels'}")
    print("-" * 30)
    bar_chars = {"INFO": "🟢", "WARNING": "🟡", "ERROR": "🔴", "DEBUG": "🔵"}
    for level, count in sorted(stats["level_counts"].items()):
        bar  = bar_chars.get(level, "⚪") * count
        print(f"  {level:<10} {count:>3}   {bar}")

    print(f"\n{'🔴  Errors ({})'.format(stats['error_count'])}")
    print("-" * 30)
    for e in stats["errors"]:
        print(f"  [{e['time']}] {e['message']}")

    print(f"\n{'🟡  Warnings ({})'.format(stats['warning_count'])}")
    print("-" * 30)
    for w in stats["warnings"]:
        print(f"  [{w['time']}] {w['message']}")

    print(f"\n{'👥  Unique Users Detected'}")
    print("-" * 30)
    if stats["unique_users"]:
        for user in sorted(stats["unique_users"]):
            print(f"  • {user}")
    else:
        print("  (none found)")

    print("\n" + "=" * 56)


# ── Step 6: Save report and filtered errors to files ─────────
def save_report(stats: dict, output_dir: str = "logs") -> None:
    """Write error entries and summary report to output files."""
    out = Path(output_dir)
    out.mkdir(exist_ok=True)

    # Save error lines
    errors_path = out / "errors_only.log"
    with open(errors_path, "w", encoding="utf-8") as f:
        f.write(f"# ERROR entries extracted — {len(stats['errors'])} total\n")
        for e in stats["errors"]:
            f.write(f"{e['date']} {e['time']} ERROR  {e['message']}\n")
    print(f"\n💾 Errors saved  → {errors_path}")

    # Save summary report as text
    report_path = out / "summary.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("LOG ANALYSIS SUMMARY\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total entries : {stats['total_entries']}\n")
        f.write(f"Errors        : {stats['error_count']}\n")
        f.write(f"Warnings      : {stats['warning_count']}\n")
        f.write(f"Info          : {stats['info_count']}\n")
        f.write(f"Duration      : {stats['duration_mins']} mins\n")
        f.write(f"Unique users  : {', '.join(sorted(stats['unique_users']))}\n")
    print(f"💾 Summary saved → {report_path}")


# ── Main ──────────────────────────────────────────────────────
if __name__ == "__main__":
    LOG_FILE = "app.log"

    # Generate sample log
    create_sample_log(LOG_FILE)

    # Parse
    print(f"\n📂 Parsing: {LOG_FILE}")
    entries = load_log(LOG_FILE)
    print(f"   Parsed {len(entries)} entries")

    # Analyse
    stats = analyse_log(entries)

    # Report
    print_report(stats)

    # Save outputs
    save_report(stats)
```

**Expected output:**

```
✅ Sample log written → app.log

📂 Parsing: app.log
   Parsed 16 entries

========================================================
               📋  LOG FILE ANALYSIS REPORT
========================================================

📊  Overview
------------------------------
  Total entries         : 16
  Time range            : 08:00:01 → 08:30:00
  Duration              : 30.0 minutes

📈  Log Levels
------------------------------
  ERROR       4   🔴🔴🔴🔴
  INFO        9   🟢🟢🟢🟢🟢🟢🟢🟢🟢
  WARNING     3   🟡🟡🟡

🔴  Errors (4)
------------------------------
  [08:07:45] Database connection timeout after 30s
  [08:10:33] FileNotFoundError: config.yaml not found
  [08:16:20] ConnectionRefusedError: Redis unreachable
  [08:25:00] Timeout: external API did not respond

🟡  Warnings (3)
------------------------------
  [08:03:22] High memory usage: 82%
  [08:12:01] API rate limit at 90%
  [08:20:11] Slow query detected: 4.2s

👥  Unique Users Detected
------------------------------
  • alice@example.com
  • bob@test.org
  • carol@company.com
  • dave@example.com
  • eve@test.org

========================================================

💾 Errors saved  → logs/errors_only.log
💾 Summary saved → logs/summary.txt
```

---

## 🚀 Bonus Challenges

```python
from pathlib import Path
import os, json

# 1. Count lines, words, chars in any file (like Unix wc)
def word_count(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.splitlines()
    words = content.split()
    return {
        "lines": len(lines),
        "words": len(words),
        "chars": len(content),
        "chars_no_spaces": len(content.replace(" ", "").replace("\n", "")),
    }

print(word_count("app.log"))

# 2. Backup a file with a timestamp
from datetime import datetime

def backup_file(src: str) -> str:
    """Copy a file adding a timestamp suffix."""
    p = Path(src)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = p.parent / f"{p.stem}_{ts}{p.suffix}"
    backup.write_bytes(p.read_bytes())
    return str(backup)

print(backup_file("app.log"))   # app_20241201_082500.log

# 3. Find all files larger than N bytes
def find_large_files(directory: str, min_bytes: int = 1024) -> list:
    return [
        (str(f), f.stat().st_size)
        for f in Path(directory).rglob("*")
        if f.is_file() and f.stat().st_size >= min_bytes
    ]

for path, size in find_large_files(".", 100):
    print(f"  {size:>8} bytes  {path}")

# 4. Read and write JSON to file (config pattern)
def save_config(config: dict, path: str = "config.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

def load_config(path: str = "config.json") -> dict:
    if not Path(path).exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

config = {"app": "MyApp", "version": "1.0", "debug": False, "port": 8000}
save_config(config)
loaded = load_config()
print(loaded["app"], loaded["port"])   # MyApp 8000

# 5. Merge multiple CSV files into one
def merge_csv_files(input_dir: str, output_file: str) -> int:
    """Merge all .csv files in a directory into one file."""
    csv_files = list(Path(input_dir).glob("*.csv"))
    if not csv_files:
        return 0
    header = None
    rows = []
    for csv_path in csv_files:
        with open(csv_path, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip()]
        if not lines:
            continue
        if header is None:
            header = lines[0]
        rows.extend(lines[1:])
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        f.write("\n".join(rows) + "\n")
    return len(rows)

# total = merge_csv_files("data/", "merged.csv")
# print(f"Merged {total} rows")
```

---

## 📋 Day 7 Summary

| Concept | Syntax | Notes |
|---|---|---|
| Open file | `open("file.txt", "r")` | Always pair with `close()` or `with` |
| Read all | `f.read()` | Returns entire file as string |
| Read one line | `f.readline()` | Returns string with `\n` |
| Read all lines | `f.readlines()` | Returns list of strings |
| Write string | `f.write("text")` | Returns number of chars written |
| Write list | `f.writelines(lst)` | No auto newline between items |
| Context manager | `with open(...) as f:` | Auto-closes — always use this |
| Iterate lines | `for line in f:` | Memory-efficient; best for large files |
| Encoding | `open(..., encoding="utf-8")` | Always specify for non-ASCII |
| Write mode | `"w"` | Creates or overwrites |
| Append mode | `"a"` | Adds to end, preserves content |
| Exclusive create | `"x"` | Fails if file already exists |
| Binary mode | `"rb"` / `"wb"` | Images, PDFs, any non-text |
| CSV with stdlib | `csv.DictReader(f)` | Handles commas/quotes in values |
| Current dir | `os.getcwd()` | String path |
| Make dirs | `os.makedirs(p, exist_ok=True)` | Creates nested dirs |
| Path exists | `os.path.exists(p)` | True/False |
| Join path | `os.path.join(a, b)` | Cross-platform separator |
| Walk tree | `os.walk(dir)` | Recurse all dirs and files |
| Env variable | `os.environ.get("KEY", default)` | Safe read with fallback |
| Path object | `Path("dir/file.csv")` | pathlib — modern standard |
| Join (pathlib) | `Path("dir") / "file.csv"` | `/` operator — readable |
| Read text | `Path(p).read_text(encoding="utf-8")` | One-liner read |
| Write text | `Path(p).write_text("text", encoding="utf-8")` | One-liner write |
| Glob | `Path(".").glob("*.csv")` | Pattern match files |
| Recursive glob | `Path(".").rglob("*.py")` | Search all subdirs |
| File name | `Path(p).name` | With extension |
| File stem | `Path(p).stem` | Without extension |
| File suffix | `Path(p).suffix` | Just the extension |
| Parent dir | `Path(p).parent` | Directory containing file |

---

## 📚 Resources

- [Real Python — File I/O](https://realpython.com/read-write-files-python/)
- [Python Docs — open()](https://docs.python.org/3/library/functions.html#open)
- [Real Python — pathlib](https://realpython.com/python-pathlib/)
- [Python Docs — pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python Docs — os.path](https://docs.python.org/3/library/os.path.html)
- [Python Docs — csv module](https://docs.python.org/3/library/csv.html)

---

## ➡️ What's Next — Day 8

Tomorrow: **Error Handling & Debugging** — `try`, `except`, `finally`, custom exceptions, and the VS Code debugger.

```python
# Preview of Day 8
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
except PermissionError as e:
    print(f"No permission: {e}")
else:
    print("File read successfully!")
finally:
    print("This always runs — cleanup here.")
```

Keep going — file I/O is used in every real project: loading datasets, saving model weights, reading configs, writing reports. 🚀
