# 백준 삼성 코테 기출 (14502 - 연구소)
# 필히 다시 풀어볼 것

from collections import deque

global virus_xy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전구역 검사, visited를 넘겨주지 않았더니 인식X..
# scope에 대해 공부할 필요가 있을듯..
def safe_cnt(visited):
    cnt = 0
    q = deque()
    for x in range(n):
        for y in range(m):
            if frame[x][y] == 2:
                visited[x][y] = 1
                cnt += 1
                q.appendleft((x, y))
    while q:
        x, y = q.pop()
        for i in range(4):
            m_x = x+dx[i]
            m_y = y+dy[i]
            if 0<=m_x<n and 0<=m_y<m:
                if frame[m_x][m_y] == 0 and visited[m_x][m_y] == 0:
                    visited[m_x][m_y] = 1
                    cnt += 1
                    q.appendleft((m_x, m_y))
    # 안전 영역 리턴
    return ((m*n) - cnt - wall_cnt)

#sx, sy 활용한 미중복 조합 코드 구현
def dfs(cnt, sx, sy):
    global ans
    visited = [[0]*m for _ in range(n)]
    if cnt == 3:
        safecnt = safe_cnt(visited)
        if safecnt > ans:
            ans = safecnt
        return
    for i in range(sx, n):
        for j in range(sy, m):
            if frame[i][j] == 0:
                frame[i][j] = 1
                if j == m-1:
                    dfs(cnt+1, i+1, 0)
                else:
                    dfs(cnt+1, i, j+1)
                frame[i][j] = 0
        sy = 0

n, m = map(int, input().split())
frame = [[] for _ in range(n)]
ans = -2147000000
wall_cnt = 0

# frame 할당 & 벽 개수 파악 & 바이러스 있는 곳 방문 처리
for i in range(n):
    frame[i] = list(map(int, input().split()))
    wall_cnt += frame[i].count(1)

# 벽을 세 개 더 세울 것이므로
wall_cnt += 3
dfs(0, 0, 0)
print(ans)