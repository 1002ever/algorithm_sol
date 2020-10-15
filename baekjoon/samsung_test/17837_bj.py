# 백준 17837 새로운 게임 2 - 삼성 코테 기출

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, k = map(int, input().split())
frame_color = [[] for _ in range(n)]
frame = [[-1]*n for _ in range(n)]
horse_list = [0]*k
for i in range(n):
    frame_color[i] = list(map(int, input().split()))
for i in range(k):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    # 말 번호 0 ~ (k-1)
    if frame[x][y] == -1:
        frame[x][y] = [i]
    else:
        frame[x][y].append(i)
    # 말 방향 저장
    horse_list[i] = [x, y, z]

ans = -1
cnt = 0
while 1:
    cnt += 1
    if cnt > 1000:
        break

    for i in range(k):
        x, y, z = horse_list[i]
        idx = frame[x][y].index(i)
        if idx > 0:
            no_move = frame[x][y][:idx]
        else:
            no_move = -1
        # 이동 말, 이동하지 않는 말 셋팅
        move = frame[x][y][idx:]
        frame[x][y] = no_move
        
        # 이동 지점 할당 및 검사
        mx = x + dx[z]
        my = y + dy[z]
        # 파란색이거나 나가면 방향 전환
        if mx < 0 or mx >= n or my < 0 or my >= n or frame_color[mx][my] == 2:
            if z == 1:
                z = 2
            elif z == 2:
                z = 1
            elif z == 3:
                z = 4
            else:
                z = 3
            mx = x + dx[z]
            my = y + dy[z]
            horse_list[i][2] = z

        # 또 파란색이면 방향 바꾼채로 제자리
        if mx < 0 or mx >= n or my < 0 or my >= n or frame_color[mx][my] == 2:
            if frame[x][y] == -1:
                frame[x][y] = move
            else:
                frame[x][y] = frame[x][y] + move
            continue
        
        # 흰색일 때
        if frame_color[mx][my] == 0:
            if frame[mx][my] == -1:
                frame[mx][my] = move
            else:
                frame[mx][my] = frame[mx][my] + move
            for j in range(len(move)):
                if j == 0:
                    horse_list[move[j]] = [mx, my, z]
                else:
                    horse_list[move[j]][0] = mx
                    horse_list[move[j]][1] = my
        # 빨간색일 때
        else:
            tmp_move = []
            for j in range(len(move)):
                tmp_move.append(move.pop())
            if frame[mx][my] == -1:
                frame[mx][my] = tmp_move
            else:
                frame[mx][my] = frame[mx][my] + tmp_move
            for j in range(len(tmp_move)):
                if j == len(tmp_move)-1:
                    horse_list[tmp_move[j]] = [mx, my, z]
                else:
                    horse_list[tmp_move[j]][0] = mx
                    horse_list[tmp_move[j]][1] = my
        if frame[mx][my] != -1 and len(frame[mx][my]) >= 4:
            ans = cnt
            break
    if ans != -1:
        break

print(ans)