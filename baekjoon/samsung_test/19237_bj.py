# 백준 19237 어른 상어 - 삼성 코테 기출

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
frame = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
shark_xy = [0]*(m+1)
for i in range(n):
    frame[i] = list(map(int, input().split()))
    for j in range(n):
        if frame[i][j] != 0:
            shark_xy[frame[i][j]] = [i, j]

shark_dir = [0] + list(map(int, input().split()))
dir_prt = [0]*(m+1)

for i in range(1, m+1):
    tmp = [0]
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    dir_prt[i] = tmp

# 상어 이동 시 frame, visited, shark_xy, shark_dir 갱신 필요

sec = 0
while 1:
    sec += 1
    if sec > 1000:
        sec = -1
        break
    
    next_xy = [0]*(m+1)
    for i in range(1, m+1):
        if shark_xy[i] == 0:
            continue
        x, y = shark_xy[i]
        # 냄새 없는 이동 가능한 곳 탐색
        chk = 0
        mx, my = x, y
        dir = -1
        for j in range(4):
            dir = dir_prt[i][shark_dir[i]][j]
            mx = x + dx[dir]
            my = y + dy[dir]
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            if visited[mx][my] != 0 or frame[mx][my] != 0:
                continue
            else:
                chk = 1
                break

        # 냄새 없는 곳을 못 찾았다면
        if chk == 0:
            for j in range(4):
                dir = dir_prt[i][shark_dir[i]][j]
                mx = x + dx[dir]
                my = y + dy[dir]
                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue
                if frame[mx][my] == 0 and visited[mx][my][0] == i:
                    break

        next_xy[i] = [mx, my, dir]

    for z in range(1, m+1):
        if shark_xy[z] == 0:
            continue
        x, y = shark_xy[z]
        mx, my, dir = next_xy[z]
        frame[x][y] = 0
        visited[x][y] = [z, k]
        
        if frame[mx][my] != 0:
            shark_xy[z] = 0
        else:
            frame[mx][my] = z
            shark_xy[z] = [mx, my]
            shark_dir[z] = dir

    # 1초 경과 시 냄새 1씩 제거
    for j in range(n):
        for l in range(n):
            if visited[j][l] != 0:
                visited[j][l][1] -= 1
                if visited[j][l][1] == 0:
                    visited[j][l] = 0

    # print(sec, '초 경과')
    # print('frame')
    # print(frame)
    # print('냄새현황')
    # print(visited)
    # print('상어 현황')
    # print(shark_xy)

    if shark_xy.count(0) == m:
        break
        
print(sec)