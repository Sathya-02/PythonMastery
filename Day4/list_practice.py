#list_practice.p4 Day 4 project

#-----1. Student Grade Tracker-------------
students = [
    ("sathya",[98,97,99,100]),
    ("tom",[98,90,97,92]),
    ("rahul",[91,92,93,90])
]

print("Student Grade Tracker")
for name,marks in students:
    avg = sum(marks) / len(marks)
    best = max(marks)
    status = "pass" if avg >= 90 else "fail"
    print(f"{name:<10} avg:{avg:.2f} best:{best} status:{status}  ")

#2. list comprehension pipeline
all_marks = [mark for _,marks in students for mark in marks]
passing = [mark for mark in all_marks if mark >= 90]
normalised = [(mark - min(all_marks)) / (max(all_marks) - min(all_marks)) for mark in all_marks]

print(f'All Marks: {all_marks}')
print(f'Passing Marks: {sorted(passing, reverse=True)}')
print(f'Normalised Marks: {[round(n,2) for n in normalised]}')

#3x3 matrix opertaions
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#transpose
transposed = [[matrix[i][j] for i in range(3)] for j in range(3)]
print(matrix)
print(transposed)

#double
doubled = [[x*2 for x in rows ] for rows in matrix]
print(doubled)




