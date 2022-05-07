# 성공
# 풀이시간: 15분

import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)

# 전체 회사의 개수, 경로(간선)의 개수
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# X(최종 목적지), K(중간 목적지) 입력받기
x, k = map(int, input().split())

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]
if result < INF:
    print(result)
else:
    print(-1)
