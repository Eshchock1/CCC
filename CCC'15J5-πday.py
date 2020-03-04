import math
p = int(input())
n = int(input())
dp = [[[0 for k in range(300)] for j in range(300)] for i in range(300)]

def splitPies(pies, people, given):
    if pies == 0:
        return 1
    if people == 0:
        return 0
    temp = 0
    if dp[pies][people][given] != 0:
        return dp[pies][people][given]
    for i in range(given, math.floor(pies/people)+1):
        dp[pies][people][given] += splitPies(pies-i, people-1, i)
    return(dp[pies][people][given])

if p == 1 or p == n:
    print(1)
else:
    print(splitPies(p, n, 1))