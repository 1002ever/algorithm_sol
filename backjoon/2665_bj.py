from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    dist[0][0] += 1
    while q:
        x, y = q.pop()
        if (x, y) == (n-1, n-1):
            print(dist[x][y])
            return
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            mx, my = x+dx, y+dy
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            if dist[mx][my] == -1:
                if frame[mx][my] == '1':
                    dist[mx][my] = dist[x][y]
                    q.append((mx, my))
                else:
                    dist[mx][my] = dist[x][y]+1
                    q.appendleft((mx, my))


n = int(input())
frame = ['' for _ in range(n)]
dist = [[-1]*n for _ in range(n)]
for i in range(n):
    frame[i] = input()
bfs()
