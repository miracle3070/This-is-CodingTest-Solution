# 문제 페이지 197쪽

# 가지고 있는 부품 입력
n = int(input())
n_list = list(map(int, input().split()))

# 주문이 들어온 부품 입력
m = int(input())
m_list = list(map(int, input().split()))

for target in m_list:
    if target in n_list:
        print("yes", end=" ")
    else:
        print("no ", end=" ")
