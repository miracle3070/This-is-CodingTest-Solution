current_pos = input()
current_col = int(current_pos[0], 16) - 0xa + 1
current_row = int(current_pos[1])
result = 0

rows = [x for x in range(1, 9)]
cols = [x for x in range(1, 9)]

# 위로 두 칸, 왼쪽으로 이동
moved_col = current_col - 2
moved_row = current_row - 1
if moved_col in cols and moved_row in rows:
    result += 1

# 위로 두 칸, 오른쪽으로 이동
moved_col = current_col - 2
moved_row = current_row + 1
if moved_col in cols and moved_row in rows:
    result += 1


# 아래로 두 칸, 왼쪽으로 이동
moved_col = current_col + 2
moved_row = current_row - 1
if moved_col in cols and moved_row in rows:
    result += 1


# 아래로 두 칸, 오른쪽으로 이동
moved_col = current_col + 2
moved_row = current_row + 1
if moved_col in cols and moved_row in rows:
    result += 1

# 왼쪽으로 두 칸, 위로 이동
moved_col = current_col - 1
moved_row = current_row - 2
if moved_col in cols and moved_row in rows:
    result += 1


# 왼쪽으로 두 칸, 아래로 이동
moved_col = current_col + 1
moved_row = current_row - 2
if moved_col in cols and moved_row in rows:
    result += 1


# 오른쪽으로 두 칸, 위로 이동
moved_col = current_col - 1
moved_row = current_row + 2
if moved_col in cols and moved_row in rows:
    result += 1


# 오른쪽으로 두 칸, 아래로 이동
moved_col = current_col + 1
moved_row = current_row + 2
if moved_col in cols and moved_row in rows:
    result += 1


print(result)