moves = input()

Hcounter = 0
Vcounter = 0

for move in moves:
    if move == "H":
        Hcounter+= 1
    else:
        Vcounter+= 1

Hmoves = Hcounter % 2
Vmoves = Vcounter % 2

if Hmoves == 0 and Vmoves == 0:
    print(1, 2)
    print(3, 4)
elif Hmoves == 1 and Vmoves == 0:
    print(3, 4)
    print(1, 2)
elif Hmoves == 0 and Vmoves == 1:
    print(2, 1)
    print(4, 3)
elif Hmoves == 1 and Vmoves == 1:
    print(4, 3)
    print(2, 1)