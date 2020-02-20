from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

n, m = map(int, input().split())
map = [[] for _ in range(n)]
max_h = -2147000000

def bfs(x, y):
    stage = -1
    visited[x][y] = True
    q.appendleft((x, y))
    while q:
        stage += 1
        for i in range(len(q)):
            x, y = q.pop()
            for j in range(4):
                m_x = x+dx[j]
                m_y = y+dy[j]
                if 0 <= m_x < n and 0 <= m_y < m:
                    if map[m_x][m_y] == 'L' and not visited[m_x][m_y]:
                        visited[m_x][m_y] = True
                        q.appendleft((m_x, m_y))
    return(stage)

for i in range(n):
    map[i] = input()

for i in range(n):
    for j in range(m):
        if map[i][j] == 'L':
            q = deque()
            visited = [[False]*m for _ in range(n)]
            visited[i][j] = True
            h = bfs(i,j)
            if h > max_h:
                max_h = h


print(max_h)