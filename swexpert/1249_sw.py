from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

def bfs(x, y):
    global ans

    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.pop()
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            # 범위 아웃
            if 0 > mx or mx >= n or 0 > my or my >= n:
                continue
            else:
                # 갈 수 있는 곳 중 최단 거리가 발견되면 갱신
                if visited[mx][my] > visited[x][y]+frame[mx][my]:
                    q.appendleft((mx, my))
                    visited[mx][my] = visited[x][y]+frame[mx][my]

for tc in range(1, t+1):
    n = int(input())
    frame = [[] for _ in range(n)]
    visited = [[2147000000]*n for _ in range(n)]
    for i in range(n):
        frame[i] = list(map(int, list(input())))

    bfs(0, 0)
    ans = visited[n-1][n-1]

    print('#%d'%tc, ans)