#day5.py

#Step1: Create, Access, Update - dictionary
student = {
    "name": "Angela",
    "city": "bangalore",
    "age": 25,
    "score": 98
}

#access
print(student["name"])
print(student["city"])
print(student["age"])
print(student["score"])

#key error
#print(student["mykey"]) #key error

#safe access
print(student.get("name"))
print(student.get("city"))
print(student.get("age"))
print(student.get("score"))
print(student.get("exam")) #none
print(student.get("exam", "default")) #default

#adding new key value
student["grade"] = "A"
print(student)

student["score"] = 100
print(student["score"])

#del key
del student["grade"]
print(student)

#check if key exists
print("name" in student)
print("grade" in student)
print("grade" not in student)

#len
print(len(student))

print(f"looping through dictionary")
#loop
for x in student:
    print(x)
    print(student[x])

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

#clear
#student.clear()
print(student)

print(student.values())
print(student.keys())
print(student.items())

total = sum(v for v in student.values() if isinstance(v, int))
print(total)

for key, value in student.items():
    print(f'{key}: {value}')

#pop and remove
age = student.pop("age")
print(age)

print(student)

student.popitem()
print(student)

#dict comprehension
squares = {y: y**2 for y in range(10)}
print(squares)

#transform
fruits = {"banana": 23, "apple": 40, "mango": 12}
discounted = {x : y*0.5 for x, y in fruits.items()}

print(discounted)

#word frequecy counter
text = ["raj", "tel", "app", "cat", "lion", "cat", "dog", "tel"]
word_freq = {word: text.count(word) for word in set(text)}
print(word_freq)

#creating sets
a={1,2,3,4,5,6,7,8,9}
b={23,3,7,9,10}

#duplicates silently removed
c={1,1,5,6,2,3,5,7,8,9}
print(c)

#create from list
raw=[1,2,3,4,1,2,3,5,1]
new_list=list(set(raw))
print(new_list)

#empty_set
empty_set=set()
print(empty_set)

empty_set.add(1)
print(empty_set)

#set operations 
python_dev={"sathya","ram","bob","alice"}
ml_dev={"kris","bob","alice","tom","sathya"}

union = python_dev | ml_dev
print(union)

intersection = python_dev & ml_dev
print(intersection)

difference = python_dev - ml_dev
print(difference)

symmetric_difference = python_dev ^ ml_dev
print(symmetric_difference) #one or other , not both

#membership test
print("sathya" in python_dev)
print("sathya" in ml_dev)   
print("sathya" not in python_dev)
print("sathya" not in ml_dev)   

#subset superset
print({1,2} <= a)
print(a >= {1,2})  

#add remove discard
python_dev.add("beck")
print(python_dev)

python_dev.remove("beck")
print(python_dev)

python_dev.discard("ram")
print(python_dev)



