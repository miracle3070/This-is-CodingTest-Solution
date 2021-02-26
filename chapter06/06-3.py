# 문제 페이지 180

# 입력받는 코드
n = int(input())
students = []

for _ in range(n):
    temp = input().split()
    students.append((temp[0], int(temp[1])))

# 오름차순 정렬 코드
students.sort(key = lambda a : a[1])

# 결과 출력 코드
for i in range(n):
    print(students[i][0], end=" ")