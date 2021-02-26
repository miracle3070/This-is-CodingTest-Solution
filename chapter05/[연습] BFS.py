from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    print(v, end=" ")
    
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if visited[x] == False:
                queue.append(x)
                visited[x] = True
                print(x, end=" ")

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)