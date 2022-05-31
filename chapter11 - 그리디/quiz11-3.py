# 풀이시간: 7분

import sys
sys.stdin = open("input.txt", "r")


string = input()
nums = list(map(int, string))

zero_area = 0
one_area = 0

cur = nums[0]
if cur:
    one_area += 1
else:
    zero_area += 1

for n in nums:
    if cur == n:
        continue
    else:
        if n:
            one_area += 1
        else:
            zero_area += 1
        cur = n

print(min(zero_area, one_area))