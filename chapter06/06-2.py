# 문제 페이지 178쪽

# 입력받는 코드
n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

# 내림차순 정렬
numbers.sort(reverse=True)

# 결과 출력
for i in range(n):
    print(numbers[i], end=" ")
