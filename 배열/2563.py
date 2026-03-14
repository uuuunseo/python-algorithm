paper = [[0 for _ in range(100)] for _ in range(100)]

a = int(input())

for _ in range(a):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y + 10):
            paper[i][j] = 1

result = 0
for i in paper:
    result += sum(i)

print(result)