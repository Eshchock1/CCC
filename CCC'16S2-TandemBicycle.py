question = int(input())
N = int(input())
city1 = list(map(int, input().split(" ")))
city2 = list(map(int, input().split(" ")))

city1.sort()
city2.sort()
groups = []

def maxVal(l1, l2):
    l2 = city2[::-1]
    for i in range(N):
        groups.append(max([l1[i], l2[i]]))
    return sum(groups)

def minVal(l1, l2):
    for i in range(N):
        groups.append(max([l1[i], l2[i]]))
    return sum(groups)

if (question == 1):
    print(minVal(city1, city2))

else:
    print(maxVal(city1, city2))