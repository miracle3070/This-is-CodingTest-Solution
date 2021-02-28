# 이진 탐색 알고리즘 재귀 함수 기반

def binary_search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

array = [1,2,5,6,7,9,10,13,15,17]
start = 0
end = len(array) - 1
target = 13

result = binary_search(array, target, start, end)
if result != -1:
    print("타겟 인덱스:", result)
else:
    print("타켓을 찾을 수 없습니다!")