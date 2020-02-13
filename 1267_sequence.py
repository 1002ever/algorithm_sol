def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in range(len(adj_list[v])):
        e_cnt[adj_list[v][i]] -= 1

    for i in adj_list[v]:
        if visited[i] == False and e_cnt[i] == 0:
            dfs(i)

for ts in range(1, 11):
    print('#%d'%ts, end=' ')
    V, E = map(int, input().split())
    e = list(map(int, input().split()))
    adj_list = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    e_cnt = [0] * (V+1)
    e_cnt[0] = -1  # 안 쓰는 인덱스

    for i in range(E):
        a, b = e[2*i], e[2*i+1]
        adj_list[a].append(b)
        e_cnt[b] += 1

    zero_idx= []
    for i in range(1, V+1):
        if e_cnt[i] == 0:
            zero_idx.append(i)

    for v in zero_idx:
        dfs(v)
    print('')