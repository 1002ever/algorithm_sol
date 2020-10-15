from collections import deque

def bfs(v):
    global cnt

    q = deque()
    cnt += 1
    visited.add(v)
    q.append(v)

    while q:
        v = q.pop()
        for i in range(len(adj_list[v])):
            if adj_list[v][i] not in visited:
                visited.add(adj_list[v][i])
                q.append(adj_list[v][i])

n, m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]
visited = set()
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, n+1):
    if i not in visited:
        bfs(i)
print(cnt)