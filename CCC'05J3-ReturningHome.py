locations = []
turns = []
reachedSchool = False

while not reachedSchool:
    inputA = input()
    inputB = input()
    turns.append(inputA)
    locations.append(inputB)
    if inputB == "SCHOOL":
        reachedSchool = True

locations = locations[::-1]
turns = turns[::-1]

for i in range(len(turns)):
    if i == len(turns) - 1:
        if turns[i] == "R":
            print("Turn LEFT into your HOME.")
        elif turns[i] == "L":
            print("Turn RIGHT into your HOME.")
    else:
        if turns[i] == "R":
            print("Turn LEFT onto " + locations[i+1] + " street.")
        elif turns[i] == "L":
            print("Turn RIGHT onto " + locations[i+1] + " street.")
