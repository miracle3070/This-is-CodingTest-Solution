# 이진 탐색 알고리즘 반복문 기반

array = [1,2,5,6,7,9,10,13,15,17]
start = 0
end = len(array) - 1
target = 13

result = -1
while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
        result = mid
        break
    elif array[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

if result != -1:
    print("타겟 인덱스:", result)
else:
    print("타켓을 찾을 수 없습니다!")

