# 성공
# 풀이시간: 5분

import sys
sys.stdin = open("input.txt" ,"r")


string = input()
nums = list(map(int, string))

result = 0
for n in nums:
    if result <= 1 or n <= 1:
        result += n
    else:
        result *= n

print(result)
