cases = int(input())

answers = []

def findNeighbours(graph, node, width, height):
    neighbours = []
    if(graph[node[0]][node[1]] == "*"):
        return neighbours
    elif(graph[node[0]][node[1]] == "+"):
        if(node[0]-1 >= 0):
            neighbours.append([node[0]-1, node[1]])  
        if(node[1]+1 < width):
            neighbours.append([node[0], node[1]+1])
        if(node[0]+1 < height):
            neighbours.append([node[0]+1, node[1]])
        if(node[1]-1 >= 0):
            neighbours.append([node[0], node[1]-1])
    elif(graph[node[0]][node[1]] == "|"):
        if(node[0]-1 >= 0):
            neighbours.append([node[0]-1, node[1]])
        if(node[0]+1 < height):
            neighbours.append([node[0]+1, node[1]])
    elif(graph[node[0]][node[1]] == "-"):
        if(node[1]+1 < width):
            neighbours.append([node[0], node[1]+1])
        if(node[1]-1 >= 0):
            neighbours.append([node[0], node[1]-1])
    return neighbours


def bfs(endMoves, graph, width, height):
   
    if(graph[height-1][width-1] == "*"):
        return -1

    explored = []
    queue = [[[0,0],0]]
    while queue:
        node, current_moves = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = findNeighbours(graph, node, width, height)
            if(node == [height-1, width-1]):
                    endMoves.append(current_moves)
            for neighbour in neighbours:
                queue.append([neighbour, current_moves + 1])
    endMoves.sort()
    if len(endMoves) == 0:
        return -1
    return (endMoves[0]+1)

def calc():
    height = int(input())
    width = int(input())
    vals = []
    endMoves= []
    for i in range(height):
        row = list(input())
        vals.append(row)
    answers.append(bfs(endMoves, vals, width, height))

for i in range(cases):
    calc()

for answer in answers:
    print(answer)