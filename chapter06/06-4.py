# 문제 페이지 182

# 입력 코드
n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 정렬 코드
array_a.sort()
array_b.sort(reverse=True)

# 원소 교환 코드
for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
        break

# 결과 출력
print(sum(array_a))