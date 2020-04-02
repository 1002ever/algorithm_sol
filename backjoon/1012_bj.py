dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = []
    visited[x][y] = True
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            m_x = x+dx[i]
            m_y = y+dy[i]
            if 0 <= m_x < h and 0 <= m_y < w:
                if farm[m_x][m_y] == 1 and visited[m_x][m_y] == False:
                    visited[m_x][m_y] = True
                    stack.append((m_x, m_y))

t = int(input())

for ts in range(1, t+1):
    h, w, n = map(int, input().split())
    farm = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    cnt = 0

    for i in range(n):
        x, y = map(int, input().split())
        farm[x][y] = 1

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and farm[i][j] == 1:
                cnt += 1
                dfs(i,j)
    print(cnt)