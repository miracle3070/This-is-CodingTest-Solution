# 성공
# 풀이시간: 11분

import sys
sys.stdin = open("input.txt", "r")


# 모험가 수
n = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0
cnt = 0
for i in range(n):
    target = people[i]
    cnt += 1
    if cnt == target:
        result += 1
        cnt = 0

print(result)