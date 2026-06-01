import math
n = int(input())
x = math.log2(n)
if x.is_integer():
    print("Yes")
else:
    print("No")
