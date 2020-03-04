start = list(map(int, input().split(" ")))
dest = list(map(int, input().split(" ")))

def findNeighbors(node):
    possible = []
    moves = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
    for move in moves:
        if (node[0] + move[0] <= 8 and node[0] + move[0] > 0) and (node[1] + move[1] <= 8 and node[1] + move[1] > 0):
            possible.append([node[0] + move[0], node[1] + move[1]])
    return possible

def bfs(start, dest):
    queue = [[start, 0]]
    visisted = []
    while queue:
        node, currentMoves = queue.pop(0)
        if node not in visisted:
            if node == dest:
                return currentMoves
            neighbors = findNeighbors(node)
            for neighbor in neighbors:
                queue.append([neighbor, currentMoves + 1])
    return -1


print(bfs(start, dest))
