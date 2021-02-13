n, m = list(map(int, input().split()))
table = []

for _ in range(n):
    row = list(map(int, input().split()))
    row.sort()
    table.append(row)

max = table[0][0]
for x in range(1, n):
    if max < table[x][0]:
        max = table[x][0]

print(max)