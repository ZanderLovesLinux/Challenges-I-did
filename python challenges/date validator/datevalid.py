day = int(input())
month = int(input())
year = int(input())
valid = True
leapyear = False


if month > 12 or month < 1 or day < 1 or day > 31:
    valid = False

if month == 9 or 4 or 6 or 11:
    if day > 30:
        valid = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leapyear = True
        else:
            leapyear = False
    else:
        leapyear = True
else:
    leapyear = False

if month == 2:
    if day > 28:
        if day == 29:
            if leapyear:
                pass
            else:
                valid = False
        else:
            valid = False   

if valid:
    print("Valid")
else:
    print("Invalid")