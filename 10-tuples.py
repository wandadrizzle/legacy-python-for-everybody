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
exit()
