lines = int(input())
largelist= []
printlist = []

for i in range(lines):
    printlist.append("")
for i in range(lines):
    letter = input()
    letter2 = letter.split(" ")
    largelist.append(letter2)

for i in range(lines):
    for n in range(2):
        if n == 0:
            largelist[i][n] = int(largelist[i][n])

for i in range(lines):
    for n in range(2):
        temp1 = largelist[i][n]
        if n == 1:
            print(temp1 * largelist[i][0])