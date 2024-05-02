""" REGEX notes:
Regular expressions are almost their own little programming language for searching and parsing strings.
with special characters in them that communicate your wishes to the regular expression system as to what defines “matching” and what is extracted from the matched strings
They match zero-or-more characters (in the case of the asterisk) or one-or-more of the characters (in the case of the plus sign).
.+ is a wild-card
Turning off greedy behaviour? The notion that the + and * characters in a regular expression expand outward to match the largest possible string.
The \S+ matches as many non-whitespace characters as possible.

- ^ Matches the beginning of the line.
- $ Matches the end of the line.
- . Matches any character (a wildcard).
- \s Matches a whitespace character.
- \S Matches a non-whitespace character (opposite of \s).
- * Applies to the immediately preceding character(s) and indicates to match zero or more times.
- *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”
- + Applies to the immediately preceding character(s) and indicates to match one or more times.
- +? Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.
- ? Applies to the immediately preceding character(s) and indicates to match zero or one time.
- ?? Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.
- [aeiou] Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
- [a-z0-9] You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.
- [^A-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.
- ( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().
- \b Matches the empty string, but only at the start or end of a word.
- \B Matches the empty string, but not at the start or end of a word.
- \d Matches any decimal digit; equivalent to the set [0-9].
- \D Matches any non-digit character; equivalent to the set [^0-9].
"""



#help()

import re
#print(dir(re)) #This prints out attributes AND methods

re_methods = [method for method in dir(re) if callable(getattr(re, method))]

print()
print(re_methods)
help (re.search)

print("Exercise 1")
#file_name = 'mbox-short.txt'
file_name = 'mbox.txt'
file_location = r'assets\files\{}'.format(file_name)
fhandle = open(file_location, 'r', encoding="UTF-8")
while True:
    count = 0
    fhandle.seek(0)
    expression = input("Enter a regular expression: ")
    if expression.lower() == 'done' : break
    for line in fhandle:
        line = line.rstrip()

        if re.search(expression, line):
            count += 1
    if count == 0:
        print("No lines matched your regex input.")
    else:
        print(f'{file_name} had {count} lines that matched {expression}')
    print()
fhandle.close()
print()
print("\nExercise 2")

while True:
    try:
        file_name = input("Enter file:")
        if file_name.lower() == "done": break
        file_location = r'assets\files\{}'.format(file_name)
        fhandle = open(file_location, 'r', encoding="UTF-8")

        count = 0
        total = 0
        for line in fhandle:
            line = line.strip()
            x = re.findall("^New Revision: (\d+)", line)
            if len(x) > 0:
                x = int(x[0])
                count += 1
                total += x

    except Exception as e:
        print("Error:", type(e), str(e))
    print(int(total/count), "\n")

fhandle.close()
exit()
print("Working with the 're' module by searching inside 'mbox-short.txt'\n")

fhandle = open(r'assets\files\mbox-short.txt', 'r', encoding="UTF-8")

for line in fhandle:
    line = line.rstrip()
    
    #We could have used string.find(substring, start, end)
    if line.startswith("From:"):
    #if line.find('From:') != -1:
        print(line)
    

    #if re.search('^From:.+@', line):
    #if re.search('^F..m:', line): #Special character matching
    #if re.search('^From:', line): #The caret insists that we're looking for a match at the beginning of the line 
        #print(line)
fhandle.close()
print()

f = 'From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu'
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
sample_text = """
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
          for <source@collab.sakaiproject.org>;
Received: (from apache@localhost)
Author: stephen.marquard@uct.ac.za
"""
lst_s = re.findall('\S+@\S+', s)
lst_s = re.findall(r'\S+@\S+', s)
lst_f = re.findall('\S+@\S+', f)
lst_sample_text = re.findall('\S+@\S+', sample_text)
#lst_f = re.findall('.+@', f) #['From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @'], .+ is pushy and therefore the last at is matched!
print(lst_f)
print(lst_s)
print(f"\nThere's a lot of text here and I have {len(lst_sample_text)} individual substrings:",lst_sample_text)

print("\nSearch for lines that have an at sign between characters")
fhandle = open(r'assets\files\mbox-short.txt', 'r', encoding="UTF-8")

for line in fhandle:
    line = line.rstrip()
    #line = line.translate(str.maketrans("", "", "<>;")) #You can do this for this case, but you can never really anticipate such in real life.
    #x = re.findall('\S+@\S+', line) #Make pattern better!!!
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
        #Note that the output of the program is a Python list that has a string as the single element in the list.
fhandle.close()

print("\nCombining searching and extracting")
fhandle = open(r'assets\files\mbox-short.txt', 'r', encoding="UTF-8")

for line in fhandle:
    line = line.rstrip()
   
    if re.search('^X\S*: [0-9.]+', line): #Through this we find the lines that have the numbers, how do we extract them
    #Note that inside the square brackets, the period matches an actual period (i.e., it is not a wildcard between the square brackets).
        print(line)
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        x = float(x[0])
        print(x)
        print()
    
    y = re.findall('^Details:.*rev=([0-9]+)', line) #Revision numbers ??
    if len(y) > 0:
        print("Revision number: ",y)
        print()
    z = re.findall('^From .* ([0-9][0-9]):', line)
    if len(z) > 0: print("Hour:", z, "\n")
fhandle.close()
print()
print("REGEX and the escape caharacter:")

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
exit()