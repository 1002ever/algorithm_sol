from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_des(x, y):
    global fuel
    
    q = deque()
    q.appendleft((x, y))
    visited[x][y] = 1
    cnt = 0

    while q:
        cnt += 1
        fuel -= 1
        if fuel < 0:
            return (-1, -1)
        if fuel < 0:
            return (-1, -1)
        for i in range(len(q)):
            x, y = q.pop()
            for j in range(4):
                mx = x + dx[j]
                my = y + dy[j]
                if 0 > mx or n <= mx or 0 > my or n <= my:
                    continue
                if visited[mx][my] == 0 and frame[mx][my] != 1:
                    if cur == (mx, my):
                        fuel += (2*cnt)
                        return (mx, my)
                    q.appendleft((mx, my))
                    visited[mx][my] = 1
    
    return (-1, -1)

def bfs(x, y):
    global fuel

    q = deque()
    q.appendleft((x, y))
    visited[x][y] = 1

    candidate = []

    while q:
        fuel -= 1
        if fuel < 0:
            return (-1, -1)
        for i in range(len(q)):
            x, y = q.pop()
            for j in range(4):
                mx = x + dx[j]
                my = y + dy[j]
                if 0 > mx or n <= mx or 0 > my or n <= my:
                    continue
                if visited[mx][my] == 0 and frame[mx][my] != 1:
                    if (mx, my) in dep:
                        candidate.append((mx, my))
                    q.appendleft((mx, my))
                    visited[mx][my] = 1
        
        if len(candidate) > 0:
            break
    
    if len(candidate) == 0:
        return (-1, -1)

    ret = candidate[0]
    if len(candidate) == 1:
        return ret

    for k in range(1, len(candidate)):
        if candidate[k][0] < ret[0]:
            ret = candidate[k]
            continue
        elif candidate[k][0] == ret[0] and candidate[k][1] < ret[1]:
            ret = candidate[k]
            continue
    return ret


n, m, fuel = map(int, input().split())
frame = [[] for _ in range(n)]
ans = 0

for i in range(n):
    frame[i] = list(map(int, input().split()))

# 시작 행-열
x, y = map(int, input().split())
x -= 1
y -= 1

dep = []
des = []
for i in range(m):
    a, b, c, d = map(int, input().split())
    dep.append((a-1, b-1))
    des.append((c-1, d-1))

for i in range(m):

    # 최단 거리 손님 탐색
    visited = [[0]*n for _ in range(n)]
    if (x, y) not in dep:
        x, y = bfs(x, y)
    # 탐색 중 연료 다 되면 -1, -1
    if (x, y) == (-1, -1):
        fuel = -1
        break

    idx = dep.index((x, y))
    dep.pop(idx)
    # 현 탑승 손님 목적지
    cur = des.pop(idx)

    visited = [[0]*n for _ in range(n)]
    if (x, y) != cur:
        x, y = bfs_des(x, y)
    if (x, y) == (-1, -1):
        fuel = -1
        break

print(fuel)