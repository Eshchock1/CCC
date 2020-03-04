t = int(input())
vals = []
for i in range(t):
    temp = []
    n = int(input())
    for i in range(n):
        temp.append(int(input()))
    vals.append(temp)

for i in range(t):
    river = []
    bank = []
    counter = 1
    y = len(vals[i])
    n = y
    while n > 0:
        done = False
        if len(vals[i]) > 0:
            if vals[i][-1] == counter:
                river.append(vals[i].pop(-1))
                counter+=1
                done = True
                n-=1
        if len(bank) != 0 and not done:
            if bank[-1] == counter:
                counter+=1
                river.append(bank.pop(-1))
                done = True
                n-= 1
        if not done:  
            bank.append(vals[i].pop(-1))
        done= False
        if len(vals[i]) == 0 and len(bank) > 0:
            if bank[-1] != counter:
                n = -1
    if len(river) == y:
        print("Y")
    else:
        print("N")

    
