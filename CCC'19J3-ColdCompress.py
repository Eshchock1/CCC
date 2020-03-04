lines = int(input())
largelist = []
numlist = []
charlist = []
for i in range(lines):
    largelist.append([])
for i in range(lines):
    letter = input()
    letter2 = letter.split()
    length1 = len(letter)
    numlist.append(1)
    charlist.append(letter[0])
    for y in range(1, length1):
        if letter[y] == letter[y-1]:
            numlength = len(numlist) - 1
            numlist[numlength] += 1
        elif letter[y] != letter[y - 1]:
            numlength = len(numlist) - 1
            charlength = len(charlist) - 1
            numlist.append(1)
            charlist.append(letter[y])
    for n in range(len(numlist)):
        numlist[n] = str(numlist[n])
    string1 = ""
    string2 = ""
    for x in range(len(charlist)):
        string1 += numlist[x]
        string1 += " "
        string1 += charlist[x]
        string1 += " "
    string1len = len(string1) - 1
    string2 = string1[0:string1len]
    largelist[i] = string2



    numlist.clear()
    charlist.clear()

for i in range(lines):
    print(largelist[i])
