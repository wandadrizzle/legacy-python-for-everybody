import time

print("Strings\n")
print("Video Question: ")
for n in "banana":
    print(n)

print("\nVideo Question: ")
word = "bananana"
i = word.find("na") #2
print(i)
#What is a lookup?
sentence = "I think I'll take my whiskey neat."

for char in sentence: #More elegant
    print(char, end="", flush="True") #Flush removes buffering
    time.sleep(0.5)

index = 0
while index < len(sentence):
    print(sentence[index], end="")
    index += 1

print()
last_char = sentence[-1]
first_char =sentence[0]
print("The first character: ", first_char)
print("The last character: ", last_char)

#You can slice strings ka so: <string_name>[n:m]
print(sentence[4:2]) #This will result in empty string
#Strings are immutable - so, if you MUST change them it's best to just create a new string

nursery = "Humpty Dumpty sat on a wall,"
#nursery = "Humpty Dumpty had a great fall."
print(nursery[:14] + "had a great fall.")


def count(letter, string):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    if count == 0:
        print(f"The letter \"{letter}\" wasn't found on the given string.")
    else:
        print(f'The letter \"{letter}\" appears {count} times in given string.')

count("z","Strings are an example of Python objects.")
notes = "Python has a function called dir which lists the methods available for an object. The type function shows the type of an object and the dir function shows the available methods."
count("b", notes)
print('a' in notes)
print('has' in notes)

print()
import string

alphabets = string.ascii_letters #This value is not locale-dependent.
print(alphabets)

print()
for alphabet in alphabets:
    print(f'{alphabet}: {ord(alphabet)}')
    #In terms of numbers A = 65 and a = 97, all the uppercase letters come before all the lowercase letters

print()
random_string = "    I am a string."
print("The letter 'a' appears", random_string.count('a'), "times")
print("The letter 'a' appears", 'banana'.count('a'), "times in the word 'banana'.") #Exercise 4

#https://docs.python.org/3/library/stdtypes.html#string-methods
#https://docs.python.org/3/library/string.html
print(random_string.strip().lower().startswith('i')) #can also lstrip or rstrip
print(type(random_string))
print(dir(random_string))
print()
#print(help(str.translate))

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
endofdomain = data.find(' ', atpos) #I want to find the first space after the @ sign
print(endofdomain)
domain = data[atpos + 1:endofdomain]
print(domain)

def echo():
    while True:
        line = input('> ')
        if len(line) == 0 or line[0] == '#':
            continue
        if line.lower() == 'done':
            break
        print(line)
    print('Done!\n')

print()
#echo()

print("Exercise 5")
str = 'X-DSPAM-Confidence: 0.8475'
colon_pos = str.find(':')
number = str[colon_pos + 2 : -1]
my_float = float(number)
print(type(my_float), my_float)

print("\nExercise 6") #https://docs.python.org/3/library/stdtypes.html#string-methods
#strip
sentence = '      Return a copy of the string with the leading and trailing characters removed. '
print(sentence.strip()) #White space removed
website = 'https://pypi.org/'
print(website.strip('./ghostr'))
website = 'www.example.com'
print(website.strip('.wm')) #The outermost leading and trailing chars argument values are stripped from the string.
print(website.strip('a')) #Original string will be outputted
print(website.strip('cmowz.'))

#replace
lyrics = """
Lemme hear you say
"This shit is bananas"
B-A-N-A-N-A-S
"This shit is bananas"
B-A-N-A-N-A-S
"""
print(lyrics)
print(lyrics.replace('shit','💩'))
print(lyrics.replace('A','🍌', 3))
