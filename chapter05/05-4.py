# 미완성
from collections import deque

def bfs(n, m):
    if table[n][m] == 1:
        


n, m = map(int, input().split())

table = []
for _ in range(n):
    table.append(list(map(int, list(input()))))

queue = deque()
result = bfs(n, m)
print(result)