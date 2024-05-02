#FIX MY CODE

listOfShame = [] 

while True: 
  menu = input("Add or Remove? ") 

  if(menu.strip().lower()[0]=="a"): 
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    

  else: 
    name = input("What is the name of the record to delete? ") 
    for row in listOfShame:
        print(name in listOfShame)
        if name in listOfShame[row][0]: 
            listOfShame.remove(row) # remove the whole row if name is in it


  print(listOfShame)

exit()
listOfShame = []

def prettyPrint():
  print()
  for row in listOfShame:
    for item in row:
      # item refers to each item in the column for that row
      print(f"{item:^10}", end=" | ")
      # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.

    print()

  print()


while True:
  name = input("What is your name? ")
  age = input("What is your age? ")
  pref = input("What is your computer platform? ")

  row = [name, age, pref]

  listOfShame.append(row)
  exit = input("Exit? y/n: ")

  if (exit.strip().lower()[0] == "y"):
    break
  print()
#print(listOfShame)
prettyPrint()

while True:
  menu = input(
    "Add or Remove? ")  # Gives the user a choice prompt and stores their input.

  if (
      menu.strip().lower()[0] == "a"
  ):  # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.

    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")

    row = [name, age, pref]

    listOfShame.append(row)
    # All the 'add' code is now indented, so it's part of the 'add' branch and will only run if the user enters 'a'.

  else:  # If the user doesn't choose 'a', run this new remove code instead.
    name = input(
      "What is the name of the record to delete? ")  # Get the input of a name
    for row in listOfShame:  # Use a loop to extract one row at a time

      if name in row:  # Check if the name is in the extracted row.
        listOfShame.remove(row)  # remove the whole row if name is in it
      else:
        print("There's no entry with such a name.")

  prettyPrint()

#We cannot remove an individual item in a list of lists.
