print("EXERCISE 1")


while True:
   
    try:
        file_name = input("Enter file name: ")
        if file_name.lower() == "done" : break
        file_location = r'assets\files\{}'.format(file_name)
        fhand = open(file_location, 'r')

    #I KNOW MY FILE< HENCE THE SHABBY ERROR HANDLING 🤦
        addresses = {}
        for line in fhand:
            line = line.rstrip()
            if not line.startswith('From'): continue
            split_line = line.split()
            if split_line[0] != "From": continue
            email = split_line[1]
            addresses[email] = addresses.get(email, 0) +1
    
        #print(addresses)
        email_list = []
        for k, v in addresses.items():
            email_list.append((v, k))

        email_list.sort(reverse=True)

        #print(email_list[0])
        for key, val in email_list[:1]:
            print(val, key)

        
        print()

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(type(e), str(e))




print("\nEXERCISE 2")
print("\nEXERCISE 3")

exit()
print("Tuples - immutable lists\n")

#We can now make a list of dictionaries that have a tuple as a value.

comma_seperated_list = 'a', 'b', 'c', 'd', 'e'
tuple_with_parenthesis = ('f', 'g', 'h', 'i', 'j')

print("Example 1:", comma_seperated_list, "\t", type(comma_seperated_list))
print("Example 2:", tuple_with_parenthesis, "\t", type(tuple_with_parenthesis))

#You don't have to declare a Tuple with bracket - that's done for readability.
print()
t = 'a',
print(type(t)) #<class 'tuple'>
t = ('a')
print(type(t)) #<class 'str'> MAKE SURE TO INCLUDE THE LAST COMMA!
t = tuple() #Empty tuple
print(type(t)) 

print()

t = tuple('tuple') #The argument needs to be iterable - a string, list or tuple
print(t) #('t', 'u', 'p', 'l', 'e')

friends = ["Jess", "Nick", "Schmidtt", "Coach", "Winston", "CeCe"]
t = tuple(friends)
print(t)
while True:
    print()
    try:
        index = input("Enter a number to see name in that index: ")
        if index.lower() == "done" : break
        index = int(index)
        print(t[index])
    except Exception as e: #IndexError and ValueError are the most likely
        print(type(e), str(e))

#tuple is a Python keyword as it is a name of a constructor - don't use it as a variable name
print("Sliced tuple",t[1:3])

#t[0] = "Jessica Day" #TypeError: 'tuple' object does not support item assignment, we can't modify tuples
t = ("Jessica Day",) + t[1:] #This is me essentially replacing my original tuple
print("Tried putting Jess's full name: ", t)
t = t [:] + ("Aly", "Russell", "Sam")  
print("Added the supporting cast:", t)

print()

#Notes are funny, why are these list methods and not tuple?
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)
print(res)


print(f"\nAttempting to sort the words in this sentence [{txt}] using a tuple:")
txt = txt.split()
txt_tuple = tuple(txt) #MY ORIGINAL TUPLE

txt_tuple = tuple(sorted(txt_tuple, reverse=True))
print("Sorted alphabetical in reverse: ",txt_tuple) #This outcome is good :)

#1. DECORATE
word_lengths = [(word, len(word)) for word in txt] #List of tuples
txt_tuple_len = sorted(word_lengths , key=lambda x: x[1], reverse=True)

#2. SORT
print("Sorted via word length: ", end="")
txt_list = []
for word, length in txt_tuple_len:
       print(word, end=" ") #Yay!
       txt_list.append(word)

#UNDECORATE
txt_tuple = tuple(txt_list)
print("\nSorted via word length in reverse: ", txt_tuple) #This outcome is good :)

print("\n\nComparing tuples") #Tuples are compared lexicographically - comparison done unil a difference is found
q1 = "(0, 1, 2) < (0, 3, 4):\t\t"
q2 = "(0, 1, 2000000) < (0, 3, 4):\t"

print(q1, (0, 1, 2) < (0, 3, 4))
print(q2, (0, 1, 2000000) < (0, 3, 4))


"""
DSU Pattern:
1. Decorate - tranform the data and make it sortable
2. Sort - sort it accordingly
3. Undecorate - remove the frills, get back original data!
"""

print("\nTuple Assignment")
t = ("The return keyword", "can", "output things like so.")
a, b, c = t #paranthesis omitted for stylistic vibes
print(f"Yes we {b}. Have a tuple on the left-hand-side.")

a = "Good bye! 🚶"
b = "Hello, friend. 👋"

a, b = b, a #swapping values

print(f'When I meet a person I greet them like so: {a}')
print(f'Then when all the chatting is done I say - {b}')

print()
email = 'wanda@example.com'
username, domain = email.split('@')
print("Testing domain: ", domain)
print()
#Dictionaries have a method called items that returns a list of tuples, where each tuple is a key-value pair:
d = {'b':1, 'a':10, 'c':22}
l = list()
for k, v in d.items():
     #print(v, "\t", k)
     #l.append((v, k)) # unsorted: [(1, 'b'), (10, 'a'), (22, 'c')], sorted: [(22, 'c'), (10, 'a'), (1, 'b')]
     print(k, "\t", v) 
     l.append((k, v)) #unsorted: [('b', 1), ('a', 10), ('c', 22)], sorted:[('c', 22), ('b', 1), ('a', 10)]
print("Original list:", l)
l.sort(reverse=True)
print("Sorted list:", l)
print()
print(type(d))
t = list(d.items())
print(type(t), t)

t.sort()
print("Sorted:", t)
t.sort(reverse=True)
print("Sorted - reverse:", t) #

print("\nOPENING FILES TO CHECK THE MOST COMMON WORDS - AGAIN")

try:
     fhandle = open(r'assets\files\romeo-full.txt')
     print("Checking if successfully opened:", fhandle, "\n")
except Exception as e:
     print(type(e), str(e))

word_counts = dict()

import string
#str.maketrans(x, y, z)
"""
x	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
y	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
z	Optional. A string describing which characters to remove from the original string.
"""

non_word_things = string.punctuation + string.digits
for line in fhandle:
     line = line.translate(str.maketrans("", "", non_word_things))
     line = line.lower().split()
     for word in line:
          word_counts[word] = word_counts.get(word, 0) + 1

print("These are my unique words:", word_counts, "\n")

word_counts_list = []
for k, v in word_counts.items():
     word_counts_list.append((v, k))

word_counts_list.sort(reverse=True)
print("These are my most repeated words:\n")
for k, v in word_counts_list[:10]:
     print(k, v)
fhandle.close()

print("\nUsing tuples as keys in dictionaries")

world_wonders = {
    ("41.8902° N", "12.4922° E") : "The Colosseum in Italy",
    ("30.3285° N", "35.4444° E") : "Petra in Jordan",
    ("20.6843° N", "88.5678° W") : "Chichén Itzá in Mexico",
    ("22.9519° S", "43.2105° W") : "Christ the Redeemer in Brazil",
    ("13.1632° S", "72.5453° W") : "Machu Picchu in Peru",
    ("27.1751° N", "78.0421° E") : "Taj Mahal in India",
    ("40.4319° N", "116.5704° E") : "The Great Wall of China",
    ("13.4125° N", "103.8670° E") : "Angkor Wat",
    #Keys have to be an immutable type!
}

for (lat, long), location in world_wonders.items():
     print(f'Latitude: {lat}\tLongitude: {long} \tLocation: {location}')

world_wonders["29.9792° N", "31.1342° E"] = "The Great Pyramid of Giza"
print()
for lat, long in world_wonders:
     print(lat, long, world_wonders[lat, long])

import random
travel_key = random.choice(list(world_wonders.keys()))
print(f"\nI dare you to go to see {world_wonders[travel_key]} in the next 100 days.")

#lists of tuples, lists of lists, tuples of tuples, and tuples of lists = sequences of sequences

'''USE TUPLES WHEN:
In some contexts, like a return statement, it is syntactically simpler to create a tuple than a list. In other contexts, you might prefer a list.
If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.
If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.
'''

#LIST COMPREHENSIONS ALLOW FOR SIMPLER/COMPACT CODE
print("\n")
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [ int(x) for x in list_of_ints_in_strings ]
print(sum(list_of_ints))

#Oh, hey - look at me go - this is DATA STRUCTURES moss!
exit()
