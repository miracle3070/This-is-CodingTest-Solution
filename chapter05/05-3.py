# 문제 페이지 149p

from collections import deque

def dfs(graph, r, c):
    queue = deque([(r,c)])
    graph[r][c] = True
    
    if graph[r+1][c] == 0:
        queue.append((r+1, c))
    if graph[r][c+1] == 0:
        queue.append((r, c+1))
    
    while queue:
        r1, c1 = queue.popleft()
        graph[r1][c1] = True

        if graph[r1+1][c1] == 0:
            queue.append((r1+1, c1))
        if graph[r1][c1+1] == 0:
            queue.append((r1, c1+1))



def getCount(ice_frame, n, m):
    count = 0
    while True:
        # 얼음틀에 0인 요소가 있는지 확인
        r, c = -1, -1
        for i in range(n):
            try:
                c = ice_frame[i].index(0)
                r = i
                break
            except ValueError:
                r, c = -1, -1
        
        if r == -1:
            return count
        else:
            dfs(ice_frame, r, c)
            count += 1
            print(count)


n, m = map(int, input().split())
ice_frame = []

for _ in range(n):
    row = list(map(int, (list(input()))))
    ice_frame.append(row)

result = getCount(ice_frame, n, m)
print(result)