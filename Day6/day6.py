#strings - deep dive day 6

text = " Hello python world , welcome "

#split
words = text.split()
print(words)

words_1 = text.strip().split(' , ')
print(words_1)

csv_line = "1,name,mango"
csv_data = csv_line.split(',')
print(csv_data)

joined = ' | '.join(csv_data)
print(joined)

#replace
replaced = text.replace('python', 'java')
print(replaced)

#find
idx='python is fun'.find('fun')
print(idx)

#slice
str  = 'python3.11'

#basic_slicing  start:stop:step
print(str[0])
print(str[-1])
print(str[0:6:2])
print(str[-4:])

#no index error on slicing
print("HII"[0:100])

#step 3 : regular expression
import re
text = "Call us at +91-9876543210 or email info@company.com by 2024-12-31"

#search 
match = re.search(r"\+\d{2}-\d{10}", text)
if match:
    print(match.group())

# re.findall — return ALL matches as a list
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

# re.sub — find and REPLACE with pattern
new_text = re.sub(r'\d+', 'NUM', "Price: 500 and Qty: 10")
print(new_text)

# re.match — match only at the START of string
m = re.match(r'Call', text)
print(m)

#step 4 : format string outputs
name = 'Sathya'
score = 98.178
rank = 1

#print
print(f'Name: {name}, Score: {score}, Rank: {rank}')

#number formatting
print(f'Score: {score:.2f}')
print(f'pi: {3.14159:.6f}')

