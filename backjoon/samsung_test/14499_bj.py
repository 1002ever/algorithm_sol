# 동서북남 순
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 초기 주사위
dice = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# turn 때 마다 주사위 평면도 변경
# [1][1] 이 bottom 위치, [3][1] 이 up 위치
def turn(dice, k):
    temp = [[0]*3 for _ in range(4)]
    
    if k == 1 or k == 2:
        temp[0] = dice[0][:]
        temp[2] = dice[2][:]
        if k == 1:
            temp[1] = dice[1][1:]+[dice[3][1]]
            temp[3][1] = dice[1][0]
        else:
            temp[1] = [dice[3][1]]+dice[1][:2]
            temp[3][1] = dice[1][2]

    else:
        temp[1][0] = dice[1][0]
        temp[1][2] = dice[1][2]
        if k == 3:
            temp[0][1] = dice[3][1]
            temp[1][1] = dice[0][1]
            temp[2][1] = dice[1][1]
            temp[3][1] = dice[2][1]
        else:
            temp[0][1] = dice[1][1]
            temp[1][1] = dice[2][1]
            temp[2][1] = dice[3][1]
            temp[3][1] = dice[0][1]
    
    return temp

bottom = dice[1][1]
n, m, x, y, k = map(int, input().split())
frame = [[] for _ in range(n)]

for i in range(n):
    frame[i] = list(map(int, input().split()))

move = list(map(int, input().split()))

for k in move:
    m_x = x+dx[k]
    m_y = y+dy[k]
    
    # 지도 넘어가면 skip
    if 0 > m_x or n <= m_x or 0 > m_y or m <= m_y:
        continue

    x, y = m_x, m_y
    dice = turn(dice, k)
    bottom = dice[1][1]

    if frame[x][y] == 0:
        frame[x][y] = bottom
    else:
        dice[1][1] = frame[x][y]
        frame[x][y] = 0
    print(dice[3][1])