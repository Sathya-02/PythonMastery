# -----Writing a file ----------
#open(filename,mode)
#modes: r, w , a, x, rb, wb, t, r+

f = open("test.txt", "w")
f.write("Hello. File world!\n")
f.write("Python I/O is easy")
f.close()

#reading a file
f = open("test.txt", "r")
print(f.read())
f.close()

#reading line by line
f = open("test.txt", "r")
print(f.readline())
print(f.readline())
f.close()

#read all lines
f = open("test.txt", "r")
print(f.readlines())
f.close()

#appending to a file
f = open("text.txt", "a")
f.write("Line 3 appended \n")
f.close()

#write to line
lines_to_write = ["Line 1", "Line 2", "Line 3"]
f = open("text.txt", "w")
f.writelines(lines_to_write)
f.close()

#Step 2: with statement - context manager
with open("words.txt", "w") as f:
    f.write("\n with statement \n Hello. File world!\n")
    f.write("Python I/O is easy\n")

with open("words.txt", "r") as f:
    content = f.read()   
print(content)


#iterating line-by-line
with open("words.txt", "r") as f:
    for x in f:
        print(f"Line: {x.strip()}")

#reading into clean list
with open("words.txt", 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
print(f"lines: {lines}")

#writing multiple lines cleanly
students = ["sathya", "raj", "bob", "daisy"]
with open("students.txt", "w") as f:
    for name in students:
        f.write(f"{name}\n")

with open("students.txt", "r") as f:
    print(f.read()) 

#appending new lines
with open("students.txt", "a") as f:
    f.write("tom\n")
    f.write("alice\n")

with open("students.txt", "r") as f:
    print(f.read())

#read and write at same time
with open("students.txt", "r+") as f:
    lines = f.readlines()   

with open("students.txt", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write(content.upper())  #override

with open("students.txt", "r") as f:
    print(f.read())

#encodeing - always specify for non-ASCII text
with open("tamil.txt", "w", encoding="utf-8") as f:
    f.write("தமிழ் python")

with open("tamil.txt", "r", encoding="utf-8") as f:
    print(f.read())

#step 3 - read/write csv files
#writing csv manually

headers = ["name", "age", "city"]
data = [
    ["sathya", 32, "Bangalore"],
    ["raj", 35, "Chennai"],
    ["bob", 23, "Delhi"]
]

with open("data.csv", "w", encoding="utf-8") as f:
    f.write(",".join(headers) + "\n")
    for row in data:
        f.write(",".join(map(str, row)) + "\n")

#reading
with open("data.csv", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open("data.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    headers = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines[1:]]

print(headers)
print(data)

#using csv module

#####
#write csv manually
header = ["name", "age", "city"]
data = [
    ["sathya","32","Bangalore"],
    ["raj","35","Chennai"],
    ["bob","23","Delhi"]
]

with open("data.csv", "w", encoding="utf-8") as f:
    f.write(",".join(header) + "\n")
    for row in data:
        f.write(",".join(map(str, row)) + "\n")

#read
with open("data.csv", "r", encoding="utf-8") as f:
    csvdata = f.readlines()

headerdata = csvdata[0].strip().split(",")
datarows = [row.strip().split(",") for row in csvdata[1:]]

print(f"header: {headerdata}")
print(f"data: {datarows}" )

#parse csv into list of dicts
with open("data.csv", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip]

keys = lines[0].split(",")
records = [dict(zip(keys, row.split(","))) for row in lines[1:]]

for record in records:
    print(f"name: {record['name']}, age: {record['age']}, city: {record['city']}")

#filter and analyse
chennai_data = [record for record in records if record["city"] == "Chennai"]

for record in chennai_data:
    print(f"name: {record['name']}, age: {record['age']}, city: {record['city']}")

#age
ages = [float(record["age"]) for age in records]
avg_age = sum(ages) / len(ages)
print(f"average age: {avg_age}")

#handle csv , commas in values
import csv  #stdlib csv module

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    next_row = next(reader)
    print(f"next row: {next_row}")
    data = [row for row in reader]

print(f"header: {header}")
print(f"data: {data}")  

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["sathya", 32, "Bangalore"])
    writer.writerow(["raj", 35, "Chennai"])
    writer.writerow(["bob", 23, "Delhi"])   

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

#step 4: os module
import os   

cwd = os.getcwd()
print(f"current working directory: {cwd}")

#list directory contents
content_list = os.listdir(".")
print(f"content list: {content_list}")

#check existence
file_exists = os.path.exists("data.csv")
print(f"file exists: {file_exists}")

is_file = os.path.isfile("data.csv")
print(f"is file: {is_file}")

is_dir = os.path.isdir("data.csv")
print(f"is directory: {is_dir}")

#path operations
abs_path = os.path.abspath("data.csv")
print(f"absolute path: {abs_path}")

rel_path = os.path.relpath("data.csv")
print(f"relative path: {rel_path}")

name, ext = os.path.splitext("data.csv")
print(f"name: {name}, extension: {ext}")

#join paths safely
log_path = os.path.join("logs", "app.log")
print(f"log path: {log_path}")

#ceate directories
os.makedirs("logs", exist_ok=True)

#file info - size, timestamp
file_info = os.stat("data.csv")
print(f"file size: {file_info.st_size} bytes")
print(f"last modified: {file_info.st_mtime}")

file_info1 = os.path.getsize("data.csv")
print(f"file size: {file_info1} bytes")

file_info2 = os.path.getmtime("data.csv")
print(f"last modified: {file_info2}")

#walk directory tree
for root, dirs, files in os.walk("."):
    print(f"root: {root}")
    print(f"directories: {dirs}")
    print(f"files: {files}")
    print()


for root, dirs, files in os.walk("."):
    level = root.replace(".", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")
    for file in files:
        print(f"{indent}  {file}")

#environment variables
home = os.environ.get("HOME")
print(f"home: {home}")
path = os.environ.get("PATH", "")
print(f"path: {path}")

#set env variable
os.environ["MYAPP_DEBUG"] = "True"
print(f"debug: {os.environ.get('MYAPP_DEBUG')}")

#pathlib - modern pathlib handling

from pathlib import Path

home = Path.home()
print(f"home: {home}")

cwd = Path.cwd()
print(f"current working directory: {cwd}")  

#building path with / operator
data_dir = Path(".") / "data"
print(f"data directory: {data_dir}")
csv_path = data_dir / "data.csv"
log_file  = Path(".") / "logs" / "app.log"

print(f"csv path: {csv_path}")
print(f"csv path exists: {csv_path.exists()}")
print(f"csv path resolve: {csv_path.resolve()}")
print(f"csv path exists: {csv_path.exists()}")
print(f"log_file  is file: {log_file.is_file()}")
print(f"csv path is dir: {csv_path.is_dir()}")








