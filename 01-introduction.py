#Why Program?
'''
You'll learn to also code for yourself
'''

#Hardware Architecture
import webbrowser

def openYouTube():
    video_id = "y39D4529FM4" #Hot CPU
    video_id = "9eMWG3fwiEU" #Hard Disk in Action
    youtube_url = f'http://www.youtube.com/watch?v={video_id}'

    webbrowser.open(youtube_url)

#openYouTube()

#Python as a Language
print("I am a Python developer, a Pythonista fluent in Parseltongue.\n")
x = 6
print(x)

#Elements of Python

import keyword
print("\nPython has reserved words, these are words you can't use as identifiers or variable names")
print(keyword.kwlist)
print()

y = 43
y = y + 1
print(y)

import string, random

print()
ascii_characters = string.digits + string.ascii_letters + string.punctuation
print(ascii_characters)

def password_gen(valid_characters, length):

    password = ''.join(random.choice(valid_characters) for _ in range(length))
    return password

print("\nHere's a random password for you:",password_gen(ascii_characters, 8), "\n")


string = "You can type interactively to python via a terminal or create scripts that have a .py extension."

count = 0
for char in string:
    if char in ascii_characters:
        count += 1

print(len(string))
print(count)


def create_character_dict_for_counts(valid_characters):
    char_dict = {char: 0 for char in valid_characters}
    return char_dict

character_dict = create_character_dict_for_counts(ascii_characters)
#print(character_dict)
for char in string:
    if char in character_dict.keys():
        character_dict[char] += 1

print(character_dict)
print()

r = "\033[31m" # Red
g = "\033[32m" # Green
reset = "\033[0m"
for key, value in character_dict.items():
    
    if value == max(character_dict.values()):
        print(f"\nThe most repeated character is {key}, and it is repeated {value} times.")
    #These characters appear at least once
    if value > 0 and value != (max(character_dict.values())):
        print(g + key + reset, end=" ")
    #These charactes don't appear at all
    if value == 0:
        print(r + key + reset, end=" ")


#WOOP WOOP my code be similar, I just wasn't opening a file
'''
name = input('Enter file: ')
handle = open(name, 'r')

counts =  dict()
for line in handle:
    words =  line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount =  None
bigword =  None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigcount, bigword)

'''

exit()