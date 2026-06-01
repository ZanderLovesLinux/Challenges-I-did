a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    largest = a
elif (a > b and a < c) or (a < b and a > c):
    med = a
elif a < b and a < c:
    small = a

if b > a and b > c:
    largest = b
elif (b > a and b < c) or (b < a and b > c):
    med = b
elif b < a and b < c:
    small = b

if c > a and c > b:
    largest = c
elif (c < a and c > b) or (c > a and c < b):
    med = c
elif c < a and c < b:
    small = c

if a == b and a > c:
    largest = a
    med = b
elif a == b and a < c:
    small = a
    med = b

if b == c and b > a:
    largest = b
    med = c
elif b == c and b < a:
    small = b
    med = c

if a == c and a > b:
    largest = a
    med = c
elif a == c and a < b:
    small = a
    med = c

print(str(small) + " " + str(med) + " " + str(largest))