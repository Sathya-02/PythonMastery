#Step 1: IF/ELIF/ELSE making decisions

score = 90

if score >=90:
    print(f"Grade: A")
elif score >= 70:
    print(f"Grade: B")
elif score >= 50:
    print(f"Grade: C")
else:
    print("Fail")

#Step 2: Comparison Operators
age = 18

print(age == 18)    #equal to
print(age != 18)    #not equal to
print(age > 18)     #greater than
print(age < 18)     #less than
print(age >= 18)    #greater than or equal to
print(age <= 18)    #less than or equal

#Step 3: logical operators

age = 18
has_id = True
is_member = False

# and 
if age >= 18 and has_id:
    print("Member allowed")

# or
if age >= 18 or is_member:
    print("Member allowed")

# not
if not is_member:
    print("Member not allowed")

# combining all three
if age >= 18 and (has_id or is_member):
    print("Member allowed")


#Step 4 : for Loops + range()
#basic loop
for i in range(5):
    print(i)

#loop with range
for i in range(1,6):
    print(f"range: {i}")

#loop with steps
for i in range(1,10,3):
    print(f"step: {i}")

#Loop over LIST
fruits = ['apple', 'banana', 'cherry','date', 'elderberry']
for fruit in fruits:
    print(fruit)    #print each fruit from list

#Loop with index, enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

#use sum number 1 to 20
total = 0
for i in range(1,11):
    total += i
print(total)


print("while loop:")

#Step 5: while loop + break
#basic
count = 0
while count < 5:
    print(count)
    count += 1

#with break
count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break

for i in range(9):
    if i == 3:
        continue
    print(i)

#real world scenario
while True:
    age = input("ENter your age:")
    if age.isdigit() and 1 <= int(age) <= 100:
        print(f"your age is: {age}")
        break
    else:
        print("Invalid age")
