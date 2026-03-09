arr = [list(map(int, input().split())) for _ in range(9)]
res, row, column = -1, 0, 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > res:
            res = arr[i][j]
            row = i + 1
            column = j + 1

print(res)
print(row, column)