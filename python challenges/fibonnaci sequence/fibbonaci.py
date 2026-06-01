#print n fibbonaci numbers
n = int(input())
fullnum = ""
currnum = 1
firnum = 0
secnum = 0
finalnumber = "0 1"
for i in range (0,n-2):
    firnum = secnum
    secnum = currnum
    currnum = firnum + secnum
    finalnumber = (str(finalnumber) + " " + str(currnum))

if n == 1:
    print("0")
elif n == 0:
    print("")
else:
    print(finalnumber)