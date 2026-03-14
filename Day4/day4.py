#create , access & slice
#creating lists
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
numbers = [1, 5, 7, 9, 3, 12,16, 19]
mixed = [1, "hello", 4.5, 2, "sathya"]
empty = []

#accessing lists
print(fruits[0])
print(fruits[-1])

#slicing
print(numbers[1:17])
print(numbers[:2])
print(numbers[1:])
print(numbers[::3])
print(numbers[::-1])    
print(numbers[::-2])    

#modifying elements
fruits[4] = "orange"
print(fruits)

#step2: list methods
#append
fruits.append("pineapple")
print(fruits)

fruits.append(["papaya","mulberry"])
print(fruits)

#extend
fruits.extend(["papaya","mulberry"])
print(fruits)       

#pop
num=[1, 2, 5, 90, 89, 90]
print(num.pop())
print(num)

print(num.pop(1))
print(num)

#remove
num.remove(90)
print(num)

#sort
scores = [12, 34, 45, 13, 16, 90, 75]
scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)

names = ["sathya", "larry", "tom", "tim", "apple"]
names.sort()
print(names)

names.sort(reverse=True)
print(names)

names.sort(key=len)
print(names)


#reverse
scores.reverse()
print(scores)

#sorted --> return new , .sort --> mutates
original = [1, 4, 1, 98, 12]
print(sorted(original))
print(original)

original.sort()
print(original)

#step 3 : list comprehension
#idea is to create new list by applying expression for each item with if conditions

#basic comprehensions
squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(10) if x%2 == 0]
print(evens)

#transform string
names = ["sathya", "larry", "tom", "tim", "apple"]
upper_names = [name.upper() for name in names]
print(upper_names)

upper_names_3letter = [name.upper() for name in names if len(name) == 3]
print(upper_names_3letter)

#normalise data 0-1 range
raw = [10, 20, 30, 60, 70]

normalised = [(x-min(raw))/(max(raw)-min(raw)) for x in raw]
print(normalised)

#flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9 ]]
flattened = [item for row in matrix for item in row]
print(flattened)

matrix_new  = [[1, 2, 3], [4, 5, 6], [7, 8, 9 ]]
flat_1 = [num for row in matrix_new for num in row]
print(flat_1)


#step 4: tuples vs lists
#creating tuples
tuple_ex = (1,2,3)
rgb = (255, 12, 45)
print(tuple_ex)
print(rgb)

single_tuple = (1,)
print(single_tuple)

print(tuple_ex[0])
print(tuple_ex[-1])
#unpacking  
name,age,city = ('craze', 21, 'chennai')
print(name)
print(age)
print(city)

name,age,city = ['craze', 21, 'chennai']
print(name)
print(age)
print(city)

#swap
a,b = 12,20
a,b = b,a
print(a)
print(b)
print("swap")
a,b = (12,20)
a,b = b,a
print(a)
print(b)

#funtion returning numbers
print("funtion returning numbers")
def min_max_numbers(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num

min_num, max_num = min_max_numbers([12,23,23,45,99])
print(min_num)
print(max_num)

#tuples dictionary key
print("tuples dictionary key")
locations = {
    (12,34) : 'chennai',
    (24,78) : 'bangalore'
}

print(locations[(12,34)])

#STEP 4: nested lists

#2D matrix
print('matrix')

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print 
print(matrix[1][2])
print(matrix[0][-1])

#modify
matrix[0][0] = 10
print(matrix)

#iterate rows & column
for y in matrix:
    for x in y:
        print(x, end=' ')
    print('')

for i in range(1,3):
    print(i)    

#list comprehension to build matrix
matrix_grid = [[row*col for row in range(3)] for col in range(3)]
print(matrix_grid)

#wrong way to create 2D list
bad = [[0] * 3] * 3
print(bad)
bad[0][2]=98
print(bad)

#correct way
good = [[0] * 3 for q in range(4)]
print(good)
good[0][2]=98
print(good)




