graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited_bfs = []
queue = []

def bfs(visited_bfs, graph, node):
  visited_bfs.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited_bfs:
        visited_bfs.append(neighbour)
        queue.append(neighbour)
       
print("BFS:" , end =" ")
bfs(visited_bfs, graph, 'A')
