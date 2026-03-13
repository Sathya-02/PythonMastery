#Step 1 : Install python

#Step 2 : Install VS Code

#Step 3 : Variables & Data Types

#variables - python
age = 25            #int
price = 12.99       #float
name = "Daisy"      #string
is_active = True    #boolean
result = None       #none

#print values
print(age)
print(price)
print(name)
print(is_active)
print(result)

#print type
print(type(age))
print(type(price))
print(type(name))
print(type(is_active))

#Step 4 : Type Conversions

#type-conversions example
user_input = "25"       #this is string
age = int(user_input)   #now its integer
price = float("9.99")   #now its Float
age_str = str(age)      #now its String 

print(type(user_input))
print(type(age))
print(type(price))
print(type(age_str))

#critical pattern - always convert input()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")    #f-string 

#Step 5 : String formatting

name = "sathya"
age = 20
city = "chennai"
scrore = 99.567

#f- string
print(f"Hello, {name}")
print(f"Hello, {name}, you are {age} years old.")
print(f"Hello, {name}, you are {age} years old and you live in {city}.")

#format numbers
print(f"Your score is {scrore}")
print(f"Your score is {scrore:.2f}")    #2 decimal      
print(f"Your score is {scrore:.0f}%")   
print(f"Big Number: {10000000:,}")

#math inside f' string
print(f"Next year you will be {age + 1} years old.")
print(f"Is adult: {age >=18}")