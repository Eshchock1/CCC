n = int(input())
nodes = {}
find = []
finishedInput = False

for i in range(n):
    temp1 = list(map(int, input().split(" ")))
    nodes[temp1[0]] = temp1[1]

while not finishedInput:
    temp2 = list(map(int, input().split(" ")))
    if(temp2[0] == 0 and temp2[1] == 0):
        finishedInput = True
    else:
        find.append(temp2)

def bfsBoi(find, graph):
    start = find[0]
    explored = []
    queue = [[start,0]]
    while queue:
       node,current_moves = queue.pop(0)
       if node not in explored:
           explored.append(node)
           neighbours = graph[node]
           if graph[node] == find[1]:
               return current_moves
           queue.append([neighbours, current_moves + 1])
    return -1

for toFind in find:
    val = bfsBoi(toFind, nodes)
    if val == -1:
        print("No")
    else:
        print("Yes", val)


