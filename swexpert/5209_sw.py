def comb(sums, cnt):
    global ans
    if sums > ans:
        return
    if cnt == n:
        if ans > sums:
            ans = sums
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                comb(sums+costs[cnt][i], cnt+1)
                visited[i] = 0

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    costs = [[] for _ in range(n)]
    visited = [0]*n
    ans = 2147000000
    for i in range(n):
        costs[i] = list(map(int, input().split()))

    comb(0, 0)
    print('#%d'%tc, ans)