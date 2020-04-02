import sys
sys.stdin = open('input.txt', 'r')

def pcom(res, cnt):
    global pmax
    if res <= pmax:
        return

    if cnt == n:
        if res > pmax:
            pmax = res
        return

    for i in range(n):
        if visited[i] == 1:
            visited[i] -= 1
            pcom(res*pij[cnt][i]/100, cnt+1)
            visited[i] += 1

t = int(input())

for ts in range(1, t+1):
    n = int(input())
    pij = [[] for _ in range(n)]
    pmax = -2147000000
    visited = [1]*n
    for i in range(n):
        pij[i] = list(map(int, input().split()))

    pcom(1, 0)
    print('#%d'%ts, '%.6f'%(pmax*100))