from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    cnt = 0
    while q:
        cnt += 1
        for m in range(len(q)):
            x, y = q.pop()
            for z in range(4):
                m_x = x+dx[z]
                m_y = y+dy[z]
                if 0 > m_x or m_x >= N or 0 > m_y or m_y >= N:
                    continue
                if frame[m_x][m_y] == frame[x][y]+1 and visited[m_x][m_y] != 1:
                    q.append((m_x, m_y))
                    visited[m_x][m_y] = 1
    return cnt

T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    N = int(input())
    frame = [[] for _ in range(N)]
    maxn = -2147000000
    ans = 2147000000
    
    for i in range(N):
        frame[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            visited = [[0]*N for _ in range(N)]
            visited[i][j] = 1
            q = deque()
            q.append((i,j))
            temp = bfs()
            print(temp)
            if maxn <= temp and frame[i][j] < ans:
                maxn = temp
                ans = frame[i][j]

    print(ans, maxn)