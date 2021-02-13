n, m = map(int, input().split())
x, y, d = map(int, input().split())
result = 1

move = [(0, -1), (1, 0), (0, 1) ,(-1, 0)]

table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

while True:
    temp = d - 1
    if temp < 0:
        temp = 3
    
    # 왼쪽으로 이동 가능하면 왼쪽으로 전진
    dx, dy = move[temp]
    if table[x + dx][y + dy] == 0:
        d = temp
        x += dx
        y += dy
        table[x][y] = 1
        result += 1

    # 사면이 모두 1일 경우
    elif table[x+1][y] == 1 and table[x-1][y] == 1 and table[x][y+1] == 1 and table[x][y-1] == 1:
        dx = -move[d][0]
        dy = -move[d][1]
        if table[x + dx][y + dy] == 1:
            break
        x += dx
        y += dy
    else:
        d = temp

print(result)