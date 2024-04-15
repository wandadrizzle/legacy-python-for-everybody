x = 1
y = 2
print(x is not y)
print()
try:
    hours = input("Enter Hours: ")
    hours_float = float(hours)
    rate = input("Enter Rate: ")
    rate_float = float(rate)
    pay = hours_float * rate_float
    #pay = float(hours) * float(rate)
    print("Pay:", pay)
except ValueError:
    print("Error, please enter numeric input")


def get_grade(score):
    if score < 0.6:
        return 'F'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
print()
while True:
    try:
        value = input("Enter score: ")
        score = float(value)
        if value.upper() == "D":
            break
        elif score < 0.0 or score > 1.0:
            #raise ValueError("The score must be between 0.0 and 1.0")
            raise ValueError("Bad score")
        else:
            print(get_grade(score))
    except ValueError:
        print("Bad score")
    except Exception as e:
        print(str(e))
        #print(type(e), str(e))

print()
try:
    number = input("Enter a number: ")
    if int(number) % 2 == 0:
        print("You've entered an even number.")
    else:
        print("Odd.")
except Exception as e:
    print(str(e))
    print(type(e))