from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.appendleft((x,y))
    while q:
        x, y = q.pop()
        for i in range(8):
            m_x = x + dx[i]
            m_y = y + dy[i]
            if 0 <= m_x < m and 0 <= m_y < n:
                if frame[m_x][m_y] == 1 and visited[m_x][m_y] == False:
                    visited[m_x][m_y] = True
                    q.appendleft((m_x, m_y))

while 1:
    cnt = 0
    n, m = map(int, input().split())
    if (m, n) == (0, 0):
        break
    frame = [[0]*n for _ in range(m)]
    visited = [[False]*n for _ in range(m)]

    for i in range(m):
        frame[i] = list(map(int, input().split()))

    for i in range(m):
        for j in range(n):
            if frame[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                bfs(i,j)
    print(cnt)