n = int(input())
result = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = "%02d:%02d:%02d" % (h, m, s)
            if '3' in time:
                result += 1

print(result)