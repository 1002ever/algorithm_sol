# 삼성 코테 기출 ( 백준 15683 - 감시)

# CCTV 번호 별 탐색 경우의 수
dcnt = [0, 4, 2, 4, 4, 1]
# CCTV 번호 별 탐색 방향 수
dcnt2 = [0, 1, 2, 2, 3, 4]
dx = [[],
    [[-1], [1], [0], [0]],
    [[-1, 1], [0, 0]],
    [[-1, 0], [0, 1], [-1, 0], [0, 1]],
    [[-1, 0, 0], [-1, 1, 0], [1, 0, 0], [-1, 1, 0]],
    [[-1, 1, 0, 0]]
]
dy = [[],
    [[0], [0], [-1], [1]],
    [[0, 0], [-1, 1]],
    [[0, 1], [1, 0], [0, -1], [-1, 0]],
    [[0, -1, 1], [0, 0, 1], [0, -1, 1], [0, 0, -1]],
    [[0, 0, -1, 1]]
]

n, m = map(int, input().split())
state_max = [-2147000000]*(n*m+1)

def dfs(x, y, cctv_num, cnt):
    global max_cnt
    dicnt = dcnt[cctv_num]
    dicnt2 = dcnt2[cctv_num]
    temp = cnt

    for i in range(dicnt):
        visited = []
        cnt = temp
        for j in range(dicnt2):
            nx = x
            ny = y
            while 1:
                nx = nx + dx[cctv_num][i][j]
                ny = ny + dy[cctv_num][i][j]
                if (0 > nx) or (nx >= n) or (0 > ny) or (ny >= m) or (frame[nx][ny] == 6):
                    break
                if frame[nx][ny] == 0:
                    cnt += 1
                    frame[nx][ny] = 9
                    visited.append((nx, ny))

        if len(cctv_xy) > 0:
            nx, ny = cctv_xy.pop()
            dfs(nx, ny, frame[nx][ny], cnt)
            cctv_xy.append((nx, ny))
        else:
            if max_cnt < cnt:
                max_cnt = cnt
        
        for _ in range(len(visited)):
            xx, yy = visited.pop()
            frame[xx][yy] = 0
            cnt -= 1


frame = [[] for _ in range(n)]
max_cnt = -2147000000
cctv_cnt = 0
cctv_xy = []
ans = 0

for i in range(n):
    frame[i] = list(map(int, input().split()))
    cctv_cnt += (m - frame[i].count(0) - frame[i].count(6))
    ans += frame[i].count(0)
    if cctv_cnt > 0:
        for j in range(m):
            if frame[i][j] != 0 and frame[i][j] != 6:
                cctv_xy.append((i,j))
        
if len(cctv_xy) > 0:
    x, y = cctv_xy.pop()
    dfs(x, y, frame[x][y], 0)
    ans -= max_cnt
    
print(ans)