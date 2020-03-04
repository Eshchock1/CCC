chart = {}
n = int(input())
for i in range(n):
    x = int(input())
    if x in chart:
        chart[x] += 1
    else:
        chart[x] = 1

vals = sorted(chart.values())
used = []
used1 = 0
# case 1 only 2 1s
if vals[-1] == vals[-2] and vals[-1] != vals[-3]:
    for name, val in chart.items():
        if val == vals[-1]:
            used.append(name)
    used = sorted(used)
    print(abs(used[0]-used[-1]))
# case 3 1 1 and 2 2s
else:
    for name, val in chart.items():
        if val == vals[-1]:
            used1 = name
        if val == vals[-2]:
            used.append(name)
    used = sorted(used)
    print(max([abs(used1 - used[0]), abs(used1 - used[-1])]))