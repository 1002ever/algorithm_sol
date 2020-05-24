from collections import deque

t = int(input())
ans = 0

def bfs():
    global ans
    q = deque()
    q.appendleft((0, 0))
    
    while q:
        v, cost = q.pop()
        if cost > ans:
            continue
        if v == n:
            if ans > cost:
                ans = cost
        for i in range(n+1):
            if adj_mat[v][i] != 0:
                q.appendleft((i, cost+adj_mat[v][i]))


for tc in range(1, t+1):
    n, e = map(int, input().split())
    adj_mat = [[0]*(n+1) for _ in range(n+1)]
    ans = 2147000000
    for i in range(e):
        temp = list(map(int, input().split()))
        adj_mat[temp[0]][temp[1]] = temp[2]
    bfs()
    print('#%d'%tc, ans)