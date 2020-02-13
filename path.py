from collections import deque

def bfs(S):
    global ans
    q = deque()
    q.append(S)
    visited[S] = True

    while q:
        S = q.pop()
        for i in range(len(adj_list[S])):
            if visited[adj_list[S][i]] == False:
                if adj_list[S][i] == G:
                    ans = 1
                    return
                q.append(adj_list[S][i])
                visited[adj_list[S][i]] = True

global ans
T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')

    ans = 0
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    for i in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)

    S, G = map(int, input().split())

    bfs(S)
    print(ans)