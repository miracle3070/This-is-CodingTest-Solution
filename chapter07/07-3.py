# 문제 페이지 201

n, m = map(int, input().split())
tteok = list(map(int, input().split()))

start = 0
end = max(tteok)
result = -1

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for t in tteok:
        temp = t - mid
        if temp < 0:
            temp = 0
        total += temp
    
    if total < m:
        end = end - 1
    else:
        result = mid
        start = mid + 1

print(result)