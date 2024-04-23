import os, time, datetime

print("DAY 45 - TOD0 LIST MANAGEMENT")

todo_list = []

def menu():
    #1. Add, 2. View, 3. Remove, 4. Edit

    while True:
        print("\n1. Add\n2. View\n3. Remove\n4. Edit\n")

        option = input("What would you like to do? ")
        option = option.strip().lower()
        print(option)

        if option == "e" : break
        elif option == "1" or option == "add":
            add_item()
        elif option == "2" or option == "view":
            view()
        elif option == "3" or option == "remove":
            remove()
        elif option == "4" or option == "edit":
            edit()
        else:
            print("I do not recognise that option, please try again or enter 'e' to exit")

def valid_date(day, month, year):
    current_year = datetime.datetime.now().year
    
    if year < current_year:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Leap year
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 31:
            return False
    
    return True


def add_item():
    os.system('cls')
    #what, when is it due, how important
    try:
        count = 0
        what = input("Name of task? ")
        if not what:
            raise ValueError("Task name cannot be empty.")

        while True:
            due_date = input("When is it due? (DD/MM/YYYY) ")
            day, month, year = due_date.split('/')

            #print("Entered:", type(day), type(month), type(year))
            '''
            current_year = datetime.datetime.now().year
            current_month = datetime.datetime.now().month
            current_day = datetime.datetime.now().day
            '''
            #print("Current:", type(current_day), type(current_month), type(current_year))

            if day.isnumeric() and month.isnumeric() and year.isnumeric(): 
                if valid_date(int(day), int(month), int(year)) : break
             
                '''
                 if int(year) < current_year:
                    print("Are you into some back to the future things? You can't have due dates from the past.")
                elif int(year) >= current_year and int(month) <= 12 and int(day) <= 31  : break
                elif int(year) == current_year and current_month < int(month) and int(month) <= 12 : break
                elif int(year) == current_year and current_month == int(month) and current_day <= int(day) and int(day) <= 31 : break
                else:
                    print("Something is off about the given date.")
                '''
            else:
                raise ValueError("The date is not in the correct format.")

        while True:
            priority = input("What is the priority? ")
            priority = priority.capitalize()
            if priority != "High" and priority != "Medium" and priority != "Low":
                raise ValueError("Only 3 levels of priority are valid; Low, Medium & High.")
            else: break

        row = [what, due_date, priority]

        for row in todo_list:
            if what in row:
                print("You already have ")

        todo_list.append(row)
        count = (len(todo_list))
        print(f"\nYour todo list has been updated, you now have {count} item(s) todo.\n")

        time.sleep(3)
        os.system("cls") #use clear on Linux and Mac
        menu()

    except Exception as e:
        print("Error:", type(e), str(e))


def view():
    #view all, or a priority (High, Medium, Low)
    os.system("cls")

    option = input("What would you like to view?\n1. All\n2. Search by priority\n3. Go back to menu\n")

    option = option.strip().lower()
    if option == "e" : exit()
    elif option == "1":
        pass

    elif option == "2":
        while True:
            priority = input("Which priority would you like to view?\n1. High\n2. Medium\n3. Low\n")
            priority = priority.strip().lower()
            if priority == "e" : exit()
            if priority == "1":
                pass
            elif priority == "2":
                pass
            elif priority == "3":
                pass
            else:
                print("I do not recognise that option, please try again or enter 'e' to exit")

    elif option == "3":
        os.system("cls")
        menu()
    else:
        print("I do not recognise that option, please try again or enter 'e' to exit")

def remove():
    #done?
    pass

def edit():
    #changing any of the information
    pass

menu()
