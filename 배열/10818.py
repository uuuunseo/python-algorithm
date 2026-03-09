ran = int(input())
arr = list(map(int, input().split()))

# 첫 번째 방법(메모리: 129196	시간: 428)
max, min = arr[0], arr[0]

for i in range(ran):
    if arr[i] >= max:
        max = arr[i]
    if arr[i] <= min:
        min = arr[i]

print(min, max)

# 두 번째 방법 (메모리: 128172kb 시간: 316ms)
print(min(arr), max(arr))