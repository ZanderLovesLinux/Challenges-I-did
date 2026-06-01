n = int(input())
sechalf = [""]
if n % 2 == False:
    print("This number is not odd")
for i in range(1,n+1):
    if i % 2 == False:
        pass
    else:
        spacecount = (n-i)/2
        spacecount = int(spacecount)
        spaces = str(" " * spacecount)
        chars = str("*" * i)
        sechalf.append(spaces + chars)
        print(spaces + chars)
for i in range(n+1,2*n):
    if i % 2 == False:
        pass
    else:
        spacecount = (i - n)/2
        spacecount = int(spacecount)
        spaces = str(" " * spacecount)
        chars = str("*" * ((2 * n) - i))
        sechalf.append(spaces + chars)
        print(spaces + chars)