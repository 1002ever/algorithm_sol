# 백준 17143 낚시왕 - 삼성 코테 기출

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def shark_move(R, C, x, y, shark_state):
    s, d, z = shark_state
    if d == 3 or d == 4:
        for i in range(s):
            # 현 위치 끝이고 벽보고 있으면 방향 전환
            if y == 1 and d == 4:
                d = 3
            elif y == C and d == 3:
                d = 4
            y = y + dy[d]
    else:
        for i in range(s):
            # 현 위치 끝이고 벽보고 있으면 방향 전환
            if x == 1 and d == 1:
                d = 2
            elif x == R and d == 2:
                d = 1
            x = x + dx[d]
    return [x, y, s, d, z]

R, C, M = map(int, input().split())
frame = [[0]*(C+1) for _ in range(R+1)]
ans = 0
cur_col = 0

# 초기 상어 배치
for i in range(M):
    # s는 속력
    # d는 방향, 상하우좌(1,2,3,4) 순
    # z는 크기
    r, c, s, d, z = map(int, input().split())
    frame[r][c] = []
    frame[r][c].append(s)
    frame[r][c].append(d)
    frame[r][c].append(z)


for i in range(C):
    # 1. 우측 1칸 이동
    cur_col += 1
    # 2. 해당 열 가장 가까운 상어 잡이
    for j in range(1, R+1):
        if frame[j][cur_col] != 0:
            ans += frame[j][cur_col][2]
            frame[j][cur_col] = 0
            break
    # 3. 모든 상어 이동
    tmp_frame = [[0]*(C+1) for _ in range(R+1)]
    for k in range(1, R+1):
        for l in range(1, C+1):
            if frame[k][l] == 0:
                continue
            x, y, a, b, c = shark_move(R, C, k, l, frame[k][l])
            frame[k][l] = 0
            if tmp_frame[x][y] == 0:
                tmp_frame[x][y] = [a,b,c]
            else:
                if c > tmp_frame[x][y][2]:
                    tmp_frame[x][y] = [a,b,c]
                else:
                    continue
    frame = tmp_frame
print(ans)