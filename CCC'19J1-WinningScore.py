a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

a3 *= 3
b3 *= 3
a2 *= 2
b2 *= 2

ascore = a3 + a2 + a1
bscore = b3 + b2 + b1

if ascore > bscore:
    print("A")
elif bscore > ascore:
    print("B")
else:
    print("T")
