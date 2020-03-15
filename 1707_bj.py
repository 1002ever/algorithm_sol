from collections import deque

def bfs(v):
    q = deque()
    visited.add(v)
    q.appendleft(v)
    color[v] = 1

    while q:
        v = q.pop()
        for i in range(len(adj_list[v])):
            if adj_list[v][i] not in visited:
                visited.add(adj_list[v][i])
                q.appendleft(adj_list[v][i])
                color[adj_list[v][i]] = color[v] * (-1)
                continue
            elif color[adj_list[v][i]] == color[v]:
                return False
    return True


t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v+1)]
    visited = set()
    color = [0]*(v+1)
    err = 0

    for i in range(e):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    for i in range(1, v+1):
        if i not in visited:
            if not bfs(i):
                err = 1
        if err == 1:
            break
    if err == 0:
        print('YES')
    else:
        print('NO')