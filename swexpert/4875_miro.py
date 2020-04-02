from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    q.appendleft((x,y))
    while q:
        x, y = q.pop()
        for i in range(4):
            m_x = x + dx[i]
            m_y = y + dy[i]
            if 0 <= m_x < n and 0 <= m_y < n:
                if frame[m_x][m_y] == 0 and visited[m_x][m_y] == False:
                    visited[m_x][m_y] = True
                    q.appendleft((m_x, m_y))
                elif frame[m_x][m_y] == 3:
                    return 1
    return 0


for ts in range(1, t+1):
    n = int(input())
    q = deque()
    frame = [[] for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        frame[i] = list(map(int,list(input())))
        for j in range(n):
            if frame[i][j] == 2:
                start = (i,j)

    print('#%d'%ts, bfs(*start))