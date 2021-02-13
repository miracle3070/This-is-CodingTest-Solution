n, m, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort(reverse=True)
max = nums[0]
second_max = nums[1]

count = 0
sum = 0
while count < m:
    for _ in range(k):
        sum += max
        count += 1
        if count >= m:
            break
    if count < m:
        sum += second_max
        count += 1
    else:
        break

print(sum)