print("Iteration\n")

print("Video Question: ")
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

print("\nVideo Question: ")
count = 0
for i in [2,1,5]:
    count += 1
    print("This is line:", count)
    print(i)

print("\nVideo Question: ")
smallest = None #Nonexistance, a constant suggesting emptiness
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        #break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

print("\nVideo Question: ")

print(0 == 0.0)
print(0 is 0.0) #F, 'is' is strongest than '==' | 'is' demands equality in terms of value and type
print(0 is not 0.0)
#print(0 = 0.0) #This yields a SyntaxError | SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

#exit()
###################################################################################
print("Exercise 1")

def number_prompt():
    number = ''
    total = 0
    count = 0
    average = 0
    while True:
        number = input("Enter a number: ")
        if number.lower() == "done":
            break
        try:
            number = int(number)
            total += number
            count += 1
            average = total/count
            
        #except Exception as e:
        except ValueError:
            #print(type(e), str(e))
            print("Invalid input")

    print(f'{total}\t{count}\t{average}')

number_prompt()
print()

print("Exercise 2")
def max_min_number():
    numbers = []
    number = ''
    total = 0
    count = 0
    while True:
        number = input("Enter a number: ")
        if number.lower() == "done":
            break
        try:
            number = int(number)
            numbers.append(number)
            total += number
            count += 1

        except ValueError:
            print("Invalid input")

    print(f'{total}\t{count}\t{max(numbers)}\t{min(numbers)}')

max_min_number()
print()
x = 0
x = x + 1
x += 1

def countdown():
    n = 10
    import time
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1 #excluding the iterable would lead in an infinite loop
    print("Happy New Year! :)")


def polyglot_greet(lang="english"):
    print()
    if lang == "korean":
        print("안녕하세요 (Annyeonghaseyo)")
    elif lang == "zulu":
        print("Sawubona")
    elif lang == "english":
        print("Hello")
    elif lang == "german":
        print("Guten Tag")
    elif lang == "hindi":
        print("नमस्ते (Namaste)")
    elif lang == "french":
        print(" Bonjour")
    elif lang == "portuguese":
        print("Olá")
    else:
        print("I don't know that language.")
    print()


def numbers():
    n = 12
    while n > -3:
        if n == 5:
            n -= 1
            continue
        if n == -1:
            break
        print(n, end=" ")
        n -= 1
    print("Seng'qedile.\n")

polyglot_greet()
numbers()
polyglot_greet("zulu")
countdown()

print()
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

print("\nThe largest value is:", max([3, 41, 12, 9, 74, 15]))

#Other Examples:
words = ["apple", "banana", "orange", "pineapple"]
longest_word = max(words, key=len)  # Finds the longest word in the list
print("The Longest word is:", longest_word)

exit()
#NB: It's tacky to print within a function - rather return