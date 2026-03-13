#Step 1: def keyword

def greet(name, age):
    return f"Hello {name}, your age is {age}"

message = greet('sathya', 20)
print(message)

#call again
print(greet('akshay',30))

# function with no parameters
def print_divider():
    print("-" * 40)

print_divider()

#Step 2: default parameters
def greet(name, language='English'):
    if(language == 'Tamil'):
        print(f"வணக்கம் {name}")
    else:
        print(f"Hello {name}")

#call with both param
greet('sathya','Tamil')

#call with one param
greet('akshay')

#defaults must come after non-default
#def bad_greet(language='Tamil', name): #syntax error#
#    if(language == 'Tamil'):
#        print(f"வணக்கம் {name}")
#    else:
#        print(f"Hello {name}")

#Step 3: global vs local variable

name="sathya"

def greet_me():
    msg = "hello"
    print(f"{msg}, {name}")

greet_me()
#print(msg)   #msg not avaialble , local variable

#modifying inside method - global valiable
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
print(counter)

#best practice to increment by passing as param
counter_val = 1

def increment_counter(count):
    return count + 1

counter_val = increment_counter(counter_val)
print(counter_val)

#Step 4: lambda function

def square(x):
    return x*x

print(square(5))

square_lambda = lambda y: y * y
print(f"square_lambda(10) ", square_lambda(10), "test")

#sort with  key legth
students = ["sathya","ram","joy","akshay"]

students.sort(key= lambda name: len(name))
print(students)

#sorted() - with new list
nums = [-1, -7, 8, 3, -2]
sorted_abs = sorted(nums, key = lambda x: abs(x))
print(sorted_abs)

#filter
evens = list(filter(lambda x: x % 2 == 0, [1, 28, 829, 667, 992, 90]))
print(evens)

#map
double = list(map(lambda y: y * 2, nums))
print(double)

#step 5: doctring & type hints
def greet(name: str, age: int) -> str:
    return f"Hello {name}, your age is {age}"  

print(greet('sathya', 20))

#Docstring style
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the Body Mass Index (BMI) based on weight and height.

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: BMI value.
    """
    bmi = weight / (height ** 2)
    return bmi  # Return the calculated BMI

print(calculate_bmi(70, 1.65))

#access doctstring
print(calculate_bmi.__doc__)
help(calculate_bmi) 