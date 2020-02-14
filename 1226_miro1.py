dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global ans
    if frame[x][y] == '3':
        ans = 1

    for i in range(4):
        m_x = x+dx[i]
        m_y = y+dy[i]
        if 0 <= m_x < 16 and 0 <= m_y < 16:
            if frame[m_x][m_y] != '1' and  visited[m_x][m_y] == False:
                visited[m_x][m_y] = True
                dfs(m_x,m_y)


for ts in range(10):
    t = int(input())
    n = 16
    ans = 0
    frame = [[] for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        frame[i] = input()

    visited[1][1] = True
    dfs(1,1)

    print('#%d'%t, ans)