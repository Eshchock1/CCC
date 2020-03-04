goal = int(input())
number = int(input())

strokes = []
bruh = 1000000

for i in range(number):
    x = int(input(""))
    strokes.append(x)
bruh = [0] * 10000

def dp(x):
    global goal
    global number
    options = []
    if x > goal:
       return 1000000
    if x == goal:
        return 0
    else:
        if bruh[x] != 0:
            return bruh[x]   
            # print("used DP " + str(dp[x])) 
        for i in range(number):
            options.append(1+dp(x+strokes[i]))
        bruh[x] = min(options)
        return bruh[x]
        # for stroke in strokes:
        #     bruh = min(dp(x + stroke) + 1)

a = dp(0)        
if a >= 1000000:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in " + str(a) + " strokes.")
