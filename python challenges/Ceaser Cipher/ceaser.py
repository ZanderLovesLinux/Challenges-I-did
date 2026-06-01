text = input().strip()
shift = int(input())
word = ""
#print(allets[5:6]) prints f
allets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in text:
    pos = allets.index(i)
    newpos = pos + shift
    if newpos > 25:
        newpos = newpos - 26
    newchar = str(allets[newpos:newpos+1]).removeprefix("[").removeprefix("'").removesuffix("]").removesuffix("'")
    word = word + newchar
print(word)