print("Dictionaries")
#Can create indices of any type - key-value pair items
print("Video Question: Part 1 ")

'''
There's no order in dictionaries, C# calls them Property Bags
Though strings are used as keys often, other data types can be used
Dictionary literals = {key: value}
'''
dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict)

#HISTOGRAMS
print("\nVideo Question: Part 2 ")
'''
We look at data iteratively.

test = dict() #constructor? #TypeError: 'dict' object is not callable
test = {} #KeyError: 'car'

#DON'T JUST CALL A KEY THAT DOESN'T EXIST
print(test['car'])

'''

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
counts['kris'] = counts.get('kris', 0)
print(counts)

print("\nVideo Question: Part 3 ")
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
print()
for key, value in counts.items():
    if value > 10:
        print(key, value)


#redoing the which-character appears the most question:
print()
sentence = "For example, the sun goes up and then it goes down. It just felt meant to be. But everytime that happens, what do you get? You get a new day. Hey girl, I brought home a few bottles of wine since I know you needed more corks for that pinterest project. I don't carry a gun. I give you five minutes when we get there. You have a shelf life as an actor, so you have to find another way to express yourself. I fantasized about robbing banks for a long time, ever since I was a kid."
#print(dir(sentence)) #replace felt like a suitable method

sentence = sentence.replace(" ", "").lower()
sentence_list = list(sentence)
#print(sentence_list) #debugging print

most_frequent = None
mf_count = None

#chars = dict() #TypeError: 'dict' object is not callable
chars = {}
for char in sentence_list:
    chars[char] = chars.get(char, 0) + 1 #The key to compact code!
print(chars)

for char, count in chars.items():
    if mf_count is None or mf_count < count: #A max loop of sorts
        mf_count = count
        most_frequent = char

print(f"The [{most_frequent}] appears {mf_count} times(s).")

    

print("\nVideo Question: Counting Word Frequency using a Dictionary") #DONE WITH NOTES!

#The code walk-through can be found here https://www.youtube.com/watch?v=HqYAtchZrjE&t=2s
exit()
print("Exercise 2")
try:
    file_name = input("Enter file name: ")
    file_location = r'assets\files\{}'.format(file_name)
    fhand = open(file_location, 'r')
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(type(e), str(e))

days = {}
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    split_line = line.split(" ")
    if len(split_line) < 8: continue
    day = split_line[2]
    #print(day)
    days[day] = days.get(day, 0) + 1

print(days)


print("\n\nExercise 3")
try:
    file_name = input("Enter file name: ")
    file_location = r'assets\files\{}'.format(file_name)
    fhand = open(file_location, 'r')
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(type(e), str(e))


mail_log = {}
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    split_line = line.split()
    #print(split_line)
    if split_line[0] != "From": continue
    mail_log[split_line[1]] = mail_log.get(split_line[1], 0) + 1
    #print(split_line)
print(mail_log)

print("\nExercise 4")
while True:
    try:
        file_name = input("Enter file name: ")
        if file_name.lower() == "done" : break
        file_location = r'assets\files\{}'.format(file_name)
        fhand = open(file_location, 'r')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(type(e), str(e))


    mail_log = {}
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From'): continue
        split_line = line.split()
        if split_line[0] != "From": continue
        mail_log[split_line[1]] = mail_log.get(split_line[1], 0) + 1

    sent_most = max(mail_log, key=mail_log.get)
    print(sent_most, mail_log[sent_most], "\n")

print("\nExercise 5")
while True:
    try:
        file_name = input("Enter file name: ")
        if file_name.lower() == "done" : break
        file_location = r'assets\files\{}'.format(file_name)
        fhand = open(file_location, 'r')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(type(e), str(e))


    domains = {}
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From'): continue
        split_line = line.split()
        if split_line[0] != "From": continue
        email = split_line[1]
        atpos = email.find('@')
        d_key = email[atpos + 1:]
        domains[d_key] = domains.get(d_key, 0) + 1
  
    print(domains)
    print()


#More info about Hash Tables - https://www.cc4e.

empty = dict()
print(empty)

invite = dict()
print(invite)

invite["date"] = "2024-06-29" #YYYY-MM-DD
print(invite)

#print("\n", dir(invite))
invite.update({"location" : "New Holmes, PMB", "dress-code": "Casual", "message": "Bring a snack."})
print(invite)
print('date' in invite)
values = list(invite.values())
print(values)
print("Food" in values)

""" 'in'
1. Linear search algorithm, in lists
2. Hash table, in dictionaries

--insert / delete / search: Ke eng i-BIG O?
"""
print("\nThe HASH TABLE segway.")
example = {
    'a': 1,
    'b': 9,
    'c': 'nebraska',
    'd': True,
}

#insert
example['e'] = False

#delete
del example['a']

#search
print(example['c'])

#Look up the magic of Hash Tables | https://wikipedia.org/wiki/Hash_table
print("fin\n")
print("Exercise 1")

words = dict()
words_values = []
words_keys = []

count = 0
u_count = 0

try:
    fhandle = open(r'assets\files\words.txt', 'r')
    
except Exception as e:
    print(type(e), str(e))

print(fhandle)
for line in fhandle:
    line = line.split()
    for word in line:
        count += 1
        if word not in words_keys:
            u_count += 1
            words_keys.append(word)

#words = {item: None for item in words_keys}

item_number = 1
for item in words_keys:
    words[item] = item_number
    item_number += 1

words_values = list(words[key] for key in words_keys)
print(count)
print(u_count, "\n")
print(words) #DICTIONARY
words_keys.sort()
print(words_keys)

print("\nDictionary as a set of counters")
#An implementation is a way of performing a computation; some implementations are better than others

print("\n")
import string

#My ipusm has alphabets of different cases, white-space and punctuation
valid_char = string.ascii_letters + string.punctuation + string.whitespace #If there were digits I was sommer gonna use string.printable
wine_ipsum = f'maron is made primarily from Corvina grapes dried on racks before pressing. Loamy soils, which are usually preferred for growing most plants, actually produce rather flavorless wines. Tannic, full-bodied wines are described as chewy. During racking, a wine is moved to a new barrel and separated from sediment in the old one. Red wines usually trump whites in alcohol content.\nSome wines are made from rotting grapes: Botrytis, or noble rot, makes good dessert wine. Trichloroanisole, or stinky cork, is produced when chlorine used in sanitization comes into contact with natural cork-dwelling bacteria. Aroma, bouquet, nose – wine is smelly business. Smoky is usually a byproduct of oak barrels, or, less often, of drunken arson. Red wine was associated with blood by the ancient Egyptians.\nYounger grapes can instill herbaceous notes on the nose. Beaujolais, from the region that is its namesake, is made from Gamay grapes. How do you hold a wine glass? There is a right and a wrong way.\nChenin blanc is a white wine grape grown in the Loire Valley of France. The world\'s oldest person – at one hundred twenty-two – attributed her longevity to a diet of olive oil, port wine and chocolate. Red wines are well attributed to positive health benefits. Shiraz, Syrah, what\'s the difference? There is none. The term meritage is a blend of merit and heritage, and usually describes blended California wines.\nThe level of perceived sharpness is referred to as acidity by sommeliers, or "tartness" by drunks. Pinot noir is French for "black pinecone," a description of the grape\'s appearance.'

#YOU COULD HAVE PUT THE IPSUM IN TEXT FILE
valid_char_list = []
valid_char_list = [char for char in valid_char] #KEYS
text_dict = {char: 0 for char in valid_char_list}

#print(text_dict)
#print()
#print(wine_ipsum)

wine_ispsum_split = [ipsum for ipsum in wine_ipsum]
#print(wine_ispsum_split)

for i in wine_ispsum_split:
    if i in valid_char_list:
        text_dict[i] += 1

print(text_dict)

for keys, values in text_dict.items():
    pass

valid_char_list_values = []
valid_char_list_values = [value for value in text_dict.values()]
print()
print(valid_char_list_values)
print("Maximum:", max(valid_char_list_values)) #But I don't know which key this is
print("Maximum:", max(text_dict, key=text_dict.get)) 
print("Minimum:", min(valid_char_list_values))

print()
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

print(d.get('r', 0)) #Dictionaries have a method called get that takes a key and a default value.

'''cases where word not in dictionary are accounted for here
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
'''
print("\nROMEO'S DICTIONARY:")
while True:
    try:
        file = input("Enter the file name: ")
        if file.lower() == 'done' : break
        file_location = r'assets\files\{}'.format(file)
        fhandle = open(file_location, 'r')

        count_all = 0
        romeo_dict = {}
        unique_char = {}
    except Exception as e:
        print(type(e), str(e))
    print("File successfully opened", fhandle, "\n")
    for line in fhandle:
        #Break lines into a list of words
        line = line.split()
        for word in line:
            count_all += 1
            romeo_dict[word] = romeo_dict.get(word, 0) + 1
            for r in word:
                unique_char[r] = unique_char.get(r, 0) + 1
    
    print(f"There are {count_all} words in Romeo's text.")
    print(romeo_dict)
    print('Juliet' in romeo_dict.keys())
    print()
    for key in unique_char:
        if unique_char[key] > 1:
            print(key, unique_char[key])
    print()
    sorted_unique_char = list(unique_char.keys())
    sorted_unique_char.sort()
    for key in  sorted_unique_char:
        print(key, unique_char[key])
    print()
    fhandle.close()

monologue = "The stars twinkled brightly in the night sky; the moon, a silver crescent, hung low on the horizon. Did you ever wonder what lies beyond the edge of the universe? It's a question that has baffled philosophers and scientists alike. Meanwhile, the wind whispered secrets to the trees, and the river murmured softly as it flowed gently downstream. Life is full of mysteries: some hidden in the depths of the ocean, others written in the constellations above. But perhaps the greatest mystery of all is the human heart, with its capacity for love, joy, and sorrow. So let's embrace the unknown, for therein lies the beauty of life."

case_insensitive = monologue.lower()
print()
print(case_insensitive, "\n")
plain = case_insensitive.translate(case_insensitive.maketrans("", "",string.punctuation))
print(plain)

print("\nROMEO FULL TEXT")
while True:
    try:
        file = input("Enter the file name: ")
        if file.lower() == 'done' : break
        file_location = r'assets\files\{}'.format(file)
        fhandle = open(file_location, 'r')

        #count_all = 0
        romeo_dict = {}
    except Exception as e:
        print(type(e), str(e))
    print("File successfully opened", fhandle, "\n")
    for line in fhandle:
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        line = line.split()
        for word in line:
            #count_all += 1
            romeo_dict[word] = romeo_dict.get(word, 0) + 1
    
    #print(f"There are {count_all} words in Romeo's text.")
    print(romeo_dict)

    romeo_keys = list(romeo_dict.keys())

    common = max(romeo_dict, key=romeo_dict.get)
    print("\nThe word that appears the most is:", common, '\nIt appears', romeo_dict[common], "times.")
    fhandle.close()

