# 백준 19236 청소년 상어 - 삼성 코테 기출

ans = -2147000000
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(sums, frame, frame_dir, fish_xy, shark_xy):
    global ans

    # 물고기 이동
    for i in range(1, 17):
        if fish_xy[i] == 0:
            continue
        x, y = fish_xy[i]
        dir = frame_dir[x][y]
        for j in range(8):
            chk_dir = (dir + j) % 8
            mx = x + dx[chk_dir]
            my = y + dy[chk_dir]
            # 상어이거나 나갔을 때
            if mx < 0 or mx >= 4 or my < 0 or my >= 4:
                continue
            if frame[mx][my] == 'shark':
                continue
            # 이동 칸 발견 시 방향 전환 후 이동 지점과 정보 교환
            else:
                frame_dir[x][y] = chk_dir
                frame[x][y], frame[mx][my] = frame[mx][my], frame[x][y]
                frame_dir[x][y], frame_dir[mx][my] = frame_dir[mx][my], frame_dir[x][y]
                if fish_xy[frame[x][y]] != 0:
                    fish_xy[i], fish_xy[frame[x][y]] = fish_xy[frame[x][y]], fish_xy[i]
                else:
                    fish_xy[i] = [mx, my]
                break
    
    # 상어 먹이 탐색
    food_list = []
    for i in range(4):
        x, y = shark_xy
        dir = frame_dir[x][y]
        mx = x+(dx[dir]*(i+1))
        my = y+(dy[dir]*(i+1))
        if mx < 0 or mx >= 4 or my < 0 or my >= 4:
            break
        if frame[mx][my] == 0:
            pass
        else:
            food_list.append([mx, my])

    if len(food_list) == 0:
        if ans < sums:
            ans = sums
        return
    else:
        for x, y in food_list:
            bk_frame = [[] for _ in range(4)]
            bk_frame_dir = [[] for _ in range(4)]
            bk_fish_xy = fish_xy[:]

            for i in range(4):
                bk_frame[i] = frame[i][:]
                bk_frame_dir[i] = frame_dir[i][:]
            # 먹을 고기 번호
            idx = fish_xy.index([x, y])
            # 상어 위치
            be_shark = shark_xy

            # 위치 교환
            frame[be_shark[0]][be_shark[1]], frame[x][y] = 0, 'shark'
            # 해당 고기 삭제 및 상어 위치 변경
            fish_xy[idx] = 0
            shark_xy = [x, y]

            dfs(sums+idx, frame, frame_dir, fish_xy, shark_xy)
            
            frame = bk_frame
            frame_dir = bk_frame_dir
            fish_xy = bk_fish_xy
            frame[be_shark[0]][be_shark[1]], frame[x][y] = 'shark', idx
            fish_xy[idx] = [x, y]
            shark_xy = be_shark

frame = [[0]*4 for _ in range(4)]
frame_dir = [[0]*4 for _ in range(4)]
fish_xy = [0]*17
shark_xy = [0, 0]

for i in range(4):
    input_info = list(map(int, input().split()))
    for j in range(4):
        idx = j*2
        frame[i][j] = input_info[idx]
        frame_dir[i][j] = input_info[idx+1]-1
        fish_xy[frame[i][j]] = [i, j]

# 상어 초기값
sums = frame[0][0]
frame[0][0] = 'shark'
fish_xy[sums] = 0

dfs(sums, frame, frame_dir, fish_xy, shark_xy)

print(ans)