#Expressions A

test_variable = 12.2 #<- Mr Python, find some memory and store 12.2 there
test_variable = 100 #The value is overwritten here

print(test_variable)
print(test_variable + 2)
print(test_variable == 12.2)

#Expressions B
print()
width = 15
height = 12.0
print(height/3)

import os, time, math, keyword, webbrowser
time.sleep(3)
os.system('cls')
hello = 'Hello, World!'
print(hello)
print(type(hello))

print("\nExercise 2")
name = input('Enter your name: ')
print('Hello,', name)

print("\nExercise 3")
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", pay)

print("\nExercise 4")
width = 17
height = 12.0

print(width//2)
print(width/2.0)
print(height/3)
print(1 + 2 * 5)

print("\nExercise 5")
def celcius_to_fahrenheit():
    celcius = input("Which temperature [°C] would you like to convert to Fahrenheit[°F]? ")
    fahrenheit = float(celcius) * 9/5 +32
    print(fahrenheit)

celcius_to_fahrenheit()
print(math.pi)
print(len(keyword.kwlist))

url = 'https://www.py4e.com/'
webbrowser.open(url)

exit()
