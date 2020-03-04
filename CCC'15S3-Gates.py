# gets TLE
g = int(input())
p = int(input())
vals = []
for i in range(p):
    vals.append(int(input()))


def planes(l):
    counter = 0
    while True:
        if counter == l:
            return counter
        counter += 1
        bruh = 0
        for i in range(counter-1):
            if vals[i] <= vals[counter-1]:
                bruh += 1
            if bruh == vals[counter-1]:
                return counter-1
    return l

print(planes(g))