print("LISTS\n")


print("\nVideo Question:")
#Data Structures
fruit = "banana"
x = fruit[1]
print(x)

print("\nVideo Question:")
#Which method is used to add an item at the end of a list?
x = []
print(dir(x))
x.append(3) #Append object to the end of list
x.insert(0,4) #insert something at index
#There's no push method in Python, I don't even think 'new' is a keyword in Python
print(x)
print("\nVideo Question:")

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(n)
print("\nExercise 1:")
def chop(t):
    del t[0]
    #del t[-1]
    t.pop()
    return None

t = [147, 131, 190, 58, 57, 297, 19, 290, 191, 292, 92, 43, 225, 207, 247]
a = chop(t)
print(a)
print(t)

print()

def middle(t):
    del t[0]
    del t[-1]
    return t
t = [147, 131, 190, 58, 57, 297, 19, 290, 191, 292, 92, 43, 225, 207, 247]
a = middle(t)
print(a)
print(t)

print("\nDEBUGGING")
a = "                            I believe in miracles\t"
print(a.strip()) #word - string methods return a new string and leave the original alone
print(a)
#print(t.sort()) #None - most list methods modify the argument and return None
try:
    t = t.sort()
    t.append(5) #As shown above, I've essentially made a list None. So, I'd get an error here: AttributeError: 'NoneType' object has no attribute 'append'
except Exception as e:
    print(type(e), str(e))

import math
t = ["James", 621, 0.75, True, ["Playing Soccer", "Reading", "Hiking"]]
x = ["A", "Mind", 4, math.pi] 
#x = "I'm no longer a list"

#t = t + [x] #['James', 621, 0.75, True, ['Playing Soccer', 'Reading', 'Hiking'], ['A', 'Mind', 4, 3.141592653589793]]
#t.append(x) #['James', 621, 0.75, True, ['Playing Soccer', 'Reading', 'Hiking'], ['A', 'Mind', 4, 3.141592653589793]]

#t.append([x]) #['James', 621, 0.75, True, ['Playing Soccer', 'Reading', 'Hiking'], [['A', 'Mind', 4, 3.141592653589793]]], the 6th element is confusing
#t = t.append(x) #This would make t = None
#t + [x] #Changes are lost, so nexttime you print t > ['James', 621, 0.75, True, ['Playing Soccer', 'Reading', 'Hiking']]
#t = t + x  #Issues would arise if x wasn't a list > TypeError: can only concatenate list (not "str") to list
print(t)

"""
Make copies to avoid aliasing
"""

print("\nExercise 2 and 3")

fhand = open(r'assets\files\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #if len(words) == 0 or len(words) < 3 : continue
    if len(words) < 3 or len(words) == 0 : continue #The guardian comes BEFORE
    if words[0] != 'From' : continue
    print(words[2])
    count += 1

print("\nExercise 4 - Find all unique words in file: ")

def remove_duplicates(t):
    u = []
    for item in t:
        if item in u: continue
        u.append(item)
    return u


while True:
    try:
        file_name = input("Enter file: ")

        if file_name.lower() == "done" : break

        file_location = r'assets\files\{}'.format(file_name)
        fhandle = open(file_location, 'r')
    except Exception as e: #It'll most likely be a FileNotFoundError
        print(type(e), str(e), "\n")
    
    all_words = []
    for line in fhandle:
        words = line.split()
        for word in words:
            all_words.append(word)

    #DEBUGGING!
    #print(all_words)
    #print(len(all_words))
    #print(unique_words)
    #print(len(unique_words))
    
    unique_words = remove_duplicates(all_words)
    unique_words.sort()
    print(unique_words, "\n")
    fhandle.close()

print("\nExercise 5: Minimalist Email Client")
#MBOX (mail box) is a popular file format to store and share a collection of emails
fhand = open(r'assets\files\mbox-short.txt')
count = 0
emails = []
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 1 : continue
    if words[0] != 'From' : continue
    print(words[1])
    emails.append(words[1])
    count += 1

unique_emails = remove_duplicates(emails)
print(f'There were {count} lines in the file with From as the first word')
print("\nCORRESPONDENCE WAS DONE BY:")
count = 1
for email in unique_emails:
    print(f'{count}. {email}')
    count += 1

print("\nExercise 6")

numbers = []
while True:
    try:
        str_num = input("Enter a number: ")
        if str_num.lower() == "done" : break
        float_num = float(str_num)

        numbers.append(float_num)

    except Exception as e:
        print(type(e), str(e))

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

print()
#exit()

empty = [] 
example = ['spam', 2.0, 5, [10, 20], False] #Another list is nested within this list
#Lists are mutable 
example[0] = "Text has been changed"
print(example)

try:
    #print(example[7])
    print(example[2.3]) #<class 'TypeError'> list indices must be integers or slices, not float
except IndexError:
    print("Index out of range!")
except Exception as e:
    print(type(e), str(e))


print("\nTraversing a list")
for item in example:
    print(item)

print()
print(True in example)

for x in empty:
    print('This never happens.')

print("\nList operations")

a = [0, 0]
b = [1, 2, 3]
c = [4, 5, 6]
d = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
e = []
for num in range(18, 37):
    e.append(num)

import random #Just because I am extra and refuse to think of 15 random numbers for my example
f = list(range(301))
random.shuffle(f)
f_shuffled = f[:15]
#print(f_shuffled)

f = [7, 168, 235, 259, 148, 170, 218, 91, 97, 124, 237, 145, 258, 165, 197]
'''
[7, 168, 235, 259, 148, 170, 218, 91, 97, 124, 237, 145, 258, 165, 197]
[147, 131, 190, 58, 57, 297, 19, 290, 191, 292, 92, 43, 225, 207, 247]
exit()
'''

print( a * 4) #The * operator repeats a list a given number of times
print( a + b) #Concatenation
print("\nOriginal 'c' list:", c, "\nThe length of 'c' at this point is:", len(c))
c.append(d)
print("The 'c' list after 'd' appended to it", c, "\nThe length of 'c' at this point is:", len(c))
c = [4, 5, 6]
print("\nAfter reseting the value of 'c', I extended 'd':")
print("'c' after the reset", c,"\nThe length of 'c' at this point is:", len(c) )
c.extend(d)
print("The 'c' list after 'd' extened to it", c, "\nThe length of 'c' at this point is:", len(c))
print()
print(e[3:]) #Slicing, the slice selects all the elements up to, but not including, the second index. It creates a new list
#print(f.sort()) #List methods tend to always yield 'None' so don't do this!
print("Original 'f' list:", f)
f.sort()
print("Sorted 'f' list:", f) #[7, 91, 97, 124, 145, 148, 165, 168, 170, 197, 218, 235, 237, 258, 259]

#Note, at this point - b and d haven't been modified
'''
b = [1, 2, 3]
d = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
'''

print()
x = b.pop() #This will take out the last value, the pop method DOES take in an optional index argument though
print(x)
print(b) #[1, 2]

del d[3:8] #[7, 8, 9, 15, 16, 17]
d.remove(16) #[7, 8, 9, 15, 17]

try:
    del f #This DOESN'T empty the list, it erases it COMPLETELY from memory
    print(f) #Meaning this will yield a NameError
except NameError:
    print("The variable you're trying to operate on is NOT defined!")
print("\n'd'", d) #[7, 8, 9, 15, 17]

print("The length of 'd':\t", len(d))
print("The min of 'd':\t\t", min(d))
print("The max of 'd':\t\t", max(d))
print("The sum of 'd':\t\t", sum(d)) #Only works if list has numbers only!!
print("The average of 'd':\t", sum(d)/len(d))

print()
#Note nums = [] and nums = list() ARE THE SAME THING
text = "I wonder is this random string can be listified."
text_as_list = list(text)
words = text.split()
print(words)
print(text_as_list)
number = "033-264-3600"
call = number.split("-")
print(''.join(call)) #It might be a good idea to assign the join to a variable

print("\nParsing lines")
try:
    fhand = open(r'assets\files\mbox-short.txt', 'r')
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(type(e), str(e))

#print(fhand)

days = {
    "Thu": 0,
    "Fri": 0,
    "Sat": 0
}

count = 0
#Can also use split and words[0]
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    split_line = line.split(" ")
    if len(split_line) < 8: continue
    #print(line)
    #print(split_line, len(split_line))
    day = split_line[2]
    print(day)
    count += 1
    if day in days:
        days[day] += 1

report = f"\nThe search found {count} emails.\nThursday:\t{days['Thu']}\nFriday:\t\t{days['Fri']} \nSaturday:\t{days['Sat']}"

print(report)
'''Relavant lines generally have this format:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
From: stephen.marquard@uct.ac.za
From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
From: louis@media.berkeley.edu

It then becomes so after the "split"
['From', 'ray@media.berkeley.edu', 'Thu', 'Jan', '', '3', '17:07:00', '2008'] 8
['From:', 'ray@media.berkeley.edu'] 2
'''

fhand.close()

print('\nObjects and values')

a = 'value'
b = 'value'

print(a is b) #See, since strings are immutable, variables of the same VALUE will point to the same thing.

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #Lists, even those that are the same will create different OBJECTS!
print(a == b) #So, this means 'a' and 'b' are equivalent but not identical

#Aliasing can 'resolve' this, don't do that though:
c = [1, 2, 3]
d = c

c.append(4)
print(d) #[1, 2, 3, 4], this is because I have made c and d refer to the same object

print("\nList arguments")

def delete_head(t): #t is my parameter
    del t[0]

#You need to be aware of list modifications and new list creation:
languages = ["IsiZulu", "English", "Hindi", "Afrikaans", "Tamil"]
#languages.append(["German", "Xhosa", "Korean", "Portuguese", "TshiVenda", "Shona", "Sepedi"])
modification = languages.extend(["German", "Xhosa", "Korean", "Portuguese", "TshiVenda", "Shona", "Sepedi"])
print(modification) #None
print(languages) #['IsiZulu', 'English', 'Hindi', 'Afrikaans', 'Tamil', 'German', 'Xhosa', 'Korean', 'Portuguese', 'TshiVenda', 'Shona', 'Sepedi']

languages + [] #This won't change your list - as a matter of fact what is being done here will 'disappear' if it is NOT assigned to anything
l1 =  languages + []
print("\n", languages, "|" * 9, l1)
print(languages == l1)
print(languages is l1)

l2 =  languages + ["French", "Chewa"]
print("\n", languages, "|" * 9, l2)
print(languages == l2)
print(languages is l2)

def tail(t):
    return t[1:]

print()
text = "tail---"
text_tail = tail(text)
print(text_tail)
exit()