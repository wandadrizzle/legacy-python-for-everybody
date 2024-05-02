"""
2D - Lists AKA Tables
Vertical = field
Horizontal = record

listName[row index][column index]
"""

gold_text = "\033[33m"
reset = "\033[0m"
print(f"Mecca Your Nan Very Happy - Day 43 Challenge\n\n {gold_text}")
import random

bingo = []

print("Gogo's Bingo Card Generator\n")

for num in range(0, 9):
  number = random.randint(1,90)
  if number not in bingo:
    bingo.append(number)

#print(bingo)
bingo_text = f"""
{bingo[0]:^7} | {bingo[1]:^7} | {bingo[2]:^7}
{'=' * 27}
{bingo[3]:^7} | {'BINGO':^7} | {bingo[4]:^7}
{'=' * 27}
{bingo[5]:^7} | {bingo[6]:^7} | {bingo[7]:^7}
"""

print(bingo_text)

print(reset)
exit()
print(reset)
my2DList = [["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"]]

print("My entire list\n")
print(my2DList)

print()
print("This is the first person's details:", my2DList[0])

print()

for name, age, platform in my2DList:
  print("Name:", name)
  print("Age:", age)
  print("Platform:", platform)
  print()

# I can edit the list like so:
my2DList[1][2] = "Linux"
print("This is the second person's details, after platform edit:", my2DList[1])

#begin FIX MY CODE
my2DList = [
  ["Johnny", 21, "Mac"],
  ["Sian", 19, "PC"],
  ["Gethin", 17, "PC"],
]
print()
print(my2DList[0][1])
#end FIX MY CODE

print()
while True:
  try:
    index = input(
      "Enter a row index to view details associated with that user: ")
    if index.lower() == "done" or index.lower() == "exit":
      break
    index = int(index)
    print("Name:", my2DList[index][0])
    print("Age:", my2DList[index][1])
    print("Platform:", my2DList[index][2])
    print()
  except IndexError:
    print("Index out of range - pick an index between 0 and",
          len(my2DList) - 1)
  except Exception as e:
    print("Error:", type(e), str(e))
exit()
