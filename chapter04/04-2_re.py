# 성공
# 풀이시간: 10분

import sys
sys.stdin = open("input.txt", "r")

dy = (2, 2, -2, -2, 1, 1, -1, -1)
dx = (1, -1, 1, -1, 2, -2, 2, -2)

position = input()
y = int(position[1]) # 행 번호
x = int(ord(position[0]) - ord('a')) + 1 # 열 번호
result = 0

for i in range(8):
    ny = y + dy[i]
    nx = x + dx[i]
    if 1 <= ny <= 8 and 1 <= nx <= 8:
        result += 1

print(result)
