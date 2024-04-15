hello = 'Hello World'

print(min(hello))
print(max(hello))
print(len(hello))

import math, random as rand
print(math)
print()

for i in range(5):
    x =  rand.random()
    print(x, end=" ")

print("\n")
print(rand.randint(5, 10))

#def is a keyword that indicates that this is a function definition. It indicates that the following indented section of code is to be stored for later

def show_lyrics():
    print("\nGlory\nEcclesia ft. Shanny Jeann, Adam Neff, & Shannon O'Brien\n")
    print("[Verse 1]\nShow me the wonders of Your unrelenting love\nI want to know You, I want to know You more\nOpen my eyes to see how much You gave for me\nGive me new vision, give me new vision, Lord")

show_lyrics()
print()
print(show_lyrics)
print(type(show_lyrics))

print()
print(math.pow(2,3))

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        return f'Pay: {pay}'
    else:
        ot = hours - 40
        ot_pay = ot * rate * 1.5
        pay = 40 * rate + ot_pay
        return f'Pay: {pay}'

print()
try:
    hours = input("Enter Hours: ")
    hours = float(hours)

    rate = input("Enter Rate: ")
    rate = float(rate)

    print(computepay(hours, rate))
except Exception as e:
    print(type(e), str(e))

def punishment(quantity, text):
    for _ in range(quantity):
        print(text)

print()
punishment(36, "I am not a 33 year-old woman")

print()
try:
    text = input("Which text would you like to repeat over and over again?\n")
    repetitions = input("How many times would you like to repeat it? ")
    repetitions = int(repetitions)
    if repetitions > 100:
        raise ValueError("Relax, teacher would never make you type your stuff more than a 100 times!")

    punishment(repetitions, text)
except Exception as e:
    print(type(e), str(e))