n = int(input())
snail = [[0] * n for _ in range(n)]

x, y = 0, -1  # 시작 위치 (y는 첫 이동 시 0이 되도록 -1로 설정)
num = 1       # 채울 숫자
step = 1      # 방향 (1: 증가, -1: 감소)
size = n      # 현재 이동해야 할 거리

while size > 0:
    # 1. 가로 방향 이동 (y축 변화)
    for _ in range(size):
        y += step
        snail[x][y] = num
        num += 1
    
    size -= 1  # 가로 이동 후 다음 세로 이동 거리는 1 줄어듦
    
    if size <= 0: break

    # 2. 세로 방향 이동 (x축 변화)
    for _ in range(size):
        x += step
        snail[x][y] = num
        num += 1
        
    step *= -1  # 한 세트(가로+세로)가 끝나면 방향을 반대로 바꿈 (우->하 다음은 좌->상)

# 결과 출력
for row in snail:
    print(row)