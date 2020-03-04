booklength = int(input())
pages=[]
endMoves = []
chart = {}
canReach = "N"

for i in range(booklength):
    n = i + 1
    temp1 = input().split(" ")
    temp2 = list(map(int, temp1))
    temp2.pop(0)
    chart[n] = temp2

def bfs_connected_component(graph, start):
   explored = []
   queue = [[start,0]]

   while queue:

       node,current_moves = queue.pop(0)
       if node not in explored:
           explored.append(node)
           neighbours = graph[node]

           if len(neighbours) == 0:
               endMoves.append(current_moves)

           for neighbour in neighbours:
               queue.append([neighbour, current_moves + 1])
   if len(explored) == booklength:
       canReach = "Y"
   else:
       canReach = "N"

   print(canReach)
   endMoves.sort()
   print(endMoves[0] + 1)

bfs_connected_component(chart,1)