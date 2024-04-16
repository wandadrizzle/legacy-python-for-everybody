#In this chapter, we start to work with Secondary Memory (or files). Secondary memory is not erased when the power is turned off. 
import os
print("Files")

try:
    fhand = open(r'assets\files\file.txt', 'r')
    #fhand = open(r'assets\files\filo.txt', 'r') #Ayikho le file

    file_path = r'assets\files\file.txt'
    file_name = os.path.basename(file_path)
    print("\nThe file name is:", file_name)

    #Practising string matipulation for vibes
    print(file_path, "\n")
    slash_loc = file_path.rfind('\\')
    sub_file_name = file_path[slash_loc + 1 :] #up to but not including
    print("The file name is:", file_name)


    count = 0
    for line in fhand:
        count += 1
    #print("Line count:", count, "\n")
    print(f"The line count of '{file_name}' is {count}.\n")

    print(fhand, "\n")     #If the open is successful, the operating system returns us a file handle.

    fhand.seek(0) # Rewind the file pointer to the beginning of the file
    data = fhand.read()
    print(data, "\n")

    fhand.close()
except FileNotFoundError:
    print("No such file found.")
except Exception as e:
    print(f'{type(e)}: {str(e)}')



mbox_example = """
From MAILER-DAEMON Fri Jul  8 12:08:34 2011
From: Author <author@example.com>
To: Recipient <recipient@example.com>
Subject: Sample message 1
 
This is the body.
>From (should be escaped).
There are 3 lines.
 
From MAILER-DAEMON Fri Jul  8 12:08:34 2011
From: Author <author@example.com>
To: Recipient <recipient@example.com>
Subject: Sample message 2
 
This is the second body.
"""

print(len(mbox_example))

print(mbox_example.replace("To", "2️⃣"))


def read_specific_line(number, location):
    fhand = open(location)

    for _ in range(number - 1):
        fhand.readline()
    
    my_line = fhand.readline()
    fhand.close()
    #return my_line
    print(my_line)

def read_specific_line_other(number, location):
    fhand = open(location)

    lines = fhand.readlines()

    my_line = lines[number - 1]
    fhand.close()
    #return my_line
    print(my_line)

#UTF8 - character set
try:
    fhand = open(r'assets\files\mbox.txt')
    inp = fhand.read()
    print(len(inp))

    fhand.seek(0)
    first_line = fhand.readline()
    print(first_line)

    fhand.seek(0)
    for line in fhand:
        line = line.rstrip()
        #if line.startswith('From:'):
            #print(line)
        if line.find('@uct.ac.za') == -1: continue
        print(line)
    fhand.close()  

except FileNotFoundError:
    print("No such file found.")
    exit()

#X-Sieve: CMU Sieve 2.3 - Line 6
print()
read_specific_line(6, r'assets\files\mbox.txt')
read_specific_line_other(6, r'assets\files\mbox.txt') 

#Uzobona invisible newline characters
try:
    #fout = open(r'assets\files\written\output.txt', 'w')
    fout = open(r'assets\files\written\output.txt', 'a')
except Exception as e:
    print(type(e), str(e))
    exit()
print(fout)
special_text = 'Nkosi sikelel\'iAfrika!'
from datetime import datetime 
fout.write(str(datetime.now()) + " " + special_text + "\n")
fout.close()

print()
s = '1 2\t 3\n 4'
print(s)
print(repr(s))

print("\nExercise 1")
file_name = input("Enter a file name: ")
file_location = r'assets\files\{}'.format(file_name)

try:
    fhandle = open(file_location, "r")
except FileNotFoundError:
    print("File not found.")
    exit()

data = fhandle.read()
print(data.upper())
fhandle.close()

print("\nExercise 2")
while True:
    file_name = input("Enter a file name: ")

    if file_name.lower() == 'done':
        break
    file_location = r'assets\files\{}'.format(file_name)

    try:
        fhandle = open(file_location, "r")
    except FileNotFoundError:
        print("File not found.\n")
        exit()

    total_confidence = 0
    confidence_quantity = 0
    for line in fhandle:
        if line.startswith("X-DSPAM-Confidence: "):
            space = line.find(' ')
            confidence = line[space + 1: ]
            total_confidence += float(confidence)
            confidence_quantity += 1

    if confidence_quantity != 0:       
        average_confidence = total_confidence/confidence_quantity
        print("Average spam confidence:", average_confidence, "\n") 
    else:
        print("No spam confidence data found in the file.\n")

    fhandle.close()

print("\nExercise 3")
while True:
    file_name = input("Enter a file name: ")

    if file_name.lower() == 'done':
        break
    elif file_name == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    file_location = r'assets\files\{}'.format(file_name)

    try:
        fhandle = open(file_location, "r")
    except FileNotFoundError as e:
        #print(type(e), str(e))
        print("File cannot be opened:", file_name)
        #exit()

    count = 0
    for line in fhandle:
        if line.startswith("Subject: "):
            count += 1
    if count == 0:
        print("The file had zero subject lines.")
    else:
        print(f'There were {count} subject lines in {file_name}')

    fhandle.close()