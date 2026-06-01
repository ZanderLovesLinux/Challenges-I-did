ogword = input().strip()
ogcount = len(ogword)
newword = ""
x = "ilove"
y = "you"
p = x.join(y)
for l in ogword:
    newword = list(newword)
    newword.insert(0,l)
    newword = "".join(newword)
newword = str(newword)
print(newword)