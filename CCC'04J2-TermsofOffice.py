from math import *
yearX = int(input())
yearY = int(input())
dif = yearY - yearX
t = floor(dif/60)
tempYear = yearX

print("All positions change in year", yearX)
for i in range(t):
    tempYear += 60;
    print("All positions change in year", tempYear)
