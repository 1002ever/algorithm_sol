# 백준 17144 미세먼지 안녕! - 삼성 코테 기출

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())

frame = [[0]*c for _ in range(r)]
temp_frame = []

# 공기청정기 찾았는지 여부
find_chk = 0
air_idx = []
for i in range(r):
    frame[i] = list(map(int, input().split()))
    if find_chk == 0 and frame[i].count(-1) > 0:
        idx = frame[i].index(-1)
        find_chk = 1
        air_idx = [i, idx]


def spread(x, y, size):
    
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        # 바깥에 나가거나 공기청정기 있으면 확산 X
        if mx < 0 or mx >= r or my < 0 or my >= c or frame[mx][my] == -1:
            continue
        temp_frame[mx][my] += size
        frame[x][y] -= size

def flow_wind(x, y, chk):
    if chk == "up":
        dir = 0
    else:
        dir = 1

    bx, by = x, y
    ax = bx + dx[dir]
    ay = by + dy[dir]

    while frame[ax][ay] != -1:
        if bx == x and by == y:
            frame[ax][ay] = 0

        if frame[ax][ay] > 0:
            frame[bx][by] = frame[ax][ay]
            frame[ax][ay] = 0
        
        bx, by = ax, ay
        ax = bx + dx[dir]
        ay = by + dy[dir]
        if ax < 0 or ax >= r or ay < 0 or ay >= c or (chk == "up" and dir == 1 and ax > x) or (chk == "down" and dir == 0 and ax < x):
            if chk == "up":
                if dir == 0:
                    dir = 3
                elif dir == 1:
                    dir = 2
                elif dir == 3:
                    dir = 1
            else:
                if dir == 1:
                    dir = 3
                elif dir == 3:
                    dir = 0
                elif dir == 0:
                    dir = 2

            ax = bx + dx[dir]
            ay = by + dy[dir]


for sec in range(t):

    temp_frame = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            size = frame[i][j] // 5
            if size > 0:
                spread(i, j, size)

    for i in range(r):
        for j in range(c):
            frame[i][j] += temp_frame[i][j]

    # 위 바람
    # 상우하좌 순 탐색 0 -> 3 -> 1 -> 2
    # 아래 바람
    # 하우상좌 순 탐색 1 -> 3 -> 0 -> 2
    
    flow_wind(air_idx[0], air_idx[1], "up")
    flow_wind(air_idx[0]+1, air_idx[1], "down")

ans = 2
for i in range(r):
    ans += sum(frame[i])

print(ans)