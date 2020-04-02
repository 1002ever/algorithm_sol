dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
frame = [[] for _ in range(n)]
stack = []
year = -1

# 빙산 수 찾기
def dfs(x, y):
    visited[x][y] = True
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            m_x = x+dx[i]
            m_y = y+dy[i]
            ccnt = 0
            if 0 <= m_x < n and 0 <= m_y < m:
                if visited[m_x][m_y] == False and frame[m_x][m_y] > 0:
                    visited[m_x][m_y] = True
                    stack.append((m_x, m_y))
                    for j in range(4):
                        mm_x = m_x + dx[j]
                        mm_y = m_y + dy[j]
                        if 0 <= mm_x < n and 0 <= mm_y < m:
                            if frame[mm_x][mm_y] <= 0:
                                ccnt += 1
                    chk[m_x][m_y] = ccnt

for i in range(n):
    frame[i] = list(map(int, input().split()))


while 1:
    year += 1
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    chk = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if frame[i][j] > 0 and visited[i][j] == False:
                ccnt = 0 # 최초 진입 장소 주변 0 수
                cnt += 1 # 빙하 수
                if cnt >= 2:
                    break
                for k in range(4):
                    m_x = i+dx[k]
                    m_y = j+dy[k]
                    if 0 <= m_x < n and 0 <= m_y < m:
                        if frame[m_x][m_y] <= 0:
                            ccnt += 1
                chk[i][j] = ccnt
                dfs(i,j)
        if cnt >= 2:
            break
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(year)
        break
    for i in range(n):
        for j in range(m):
            if chk[i][j] > 0:
                frame[i][j] -= chk[i][j]