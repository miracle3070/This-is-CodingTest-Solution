# 성공
# 풀이시간: 20분

import sys, heapq
sys.stdin = open("input.txt", "r")
INF = int(1e9)


# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시(출발지)
n, m, c = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    # 출발지(x), 도착지(y), 소요시간(z)
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


# 다익스트라 최단경로 알고리즘 정의
def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start))

    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for linked in graph[now]:
            cost = dist + linked[1]
            if cost < distance[linked[0]]:
                distance[linked[0]] = cost
                heapq.heappush(h, (cost, linked[0]))

# 다익스트라 알고리즘 호출
dijkstra(c)

# 최종결과 출력
cnt = 0  # 메시지를 받는 도시의 총 개수
max_time = 0  # 총 걸리는 시간
for i in range(1, n+1):
    if 0 < distance[i] < INF:
        cnt += 1
    if max_time < distance[i]:
        max_time = distance[i]
print(cnt, max_time)



