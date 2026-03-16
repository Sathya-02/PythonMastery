#dict_practice - day 5

# 1 : Student database
students={
    "S0001": {"name": "Alice", "age": 20, "scores":[90, 89,95,92], "city": "mumbai"},
    "S0002": {"name": "Bob", "age": 22, "scores":[89,100,92,75], "city": "chennai"},
    "S0003": {"name": "Charlie", "age": 21, "scores":[90,98,99,92], "city": "bangalore"},
    "S0004": {"name": "David", "age": 23, "scores":[79,92,95,92],"city": "chennai"},
}

print("====STUDENT REPORT====")
for sid, info in students.items():
    avg_score = sum(info["scores"]) / len(info["scores"])
    grade = "A" if avg_score >= 90 else "B" if avg_score >= 80 else "C" if avg_score >= 70 else "D"
    print(f"Student ID: {sid} | Name: {info['name']} | Age: {info['age']} | Average Score: {avg_score:.2f} | Grade: {grade}")

#grade summary - comprehension
averages = {
    sid: sum(info["scores"]) / len(info["scores"])
    for sid, info in students.items()
}

top_students = {sid: average for sid, average in averages.items() if average >= 90}
print(f"Top Students: {top_students}")

#set operations - group by city
chennai_students = {info['name'] for sid, info in students.items() if info["city"] == "chennai"}
bangalore_students = {info['name'] for sid, info in students.items() if info["city"] == "bangalore"}
all_students = {info['name'] for sid, info in students.items() }

print(f"Chennai Students: {chennai_students}")
print(f"Bangalore Students: {bangalore_students}")
print(f"All Students: {all_students}")  
print(f"Not in chennai: {all_students - chennai_students}")
print(f"Only in One city: {chennai_students ^ bangalore_students}")

#word frequency
text = "the cat sat on the mat and the cat sat"
words = text.split()
word_freq = {word: words.count(word) for word in words}
print(word_freq)