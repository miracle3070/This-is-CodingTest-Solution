# 성공 (사실상 시간초과)
# 풀이시간: 10분
# 메모: 시간복잡도가 2^n으로 엄청 크다. (비효율적인 풀이라는 뜻)

from itertools import combinations


import sys
sys.stdin = open("input.txt", "r")


# 동전의 개수
n = int(input())
coins = list(map(int, input().split()))
memory = [0] * (sum(coins) + 1)

for coin in coins:
    memory[coin] = 1

for m in range(2, n+1):
    comb = combinations(coins, m)
    for c in comb:
        memory[sum(c)] = 1

result = 0
for i in range(1, sum(coins)+1):
    if memory[i] == 0:
        result = i
        break

print(result)