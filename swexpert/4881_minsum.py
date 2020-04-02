t = int(input())

def powset(cnt, temp):
    global min
    if cnt == n:
        if min > temp:
            min = temp
        return

    if temp > min:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            powset(cnt+1, temp+frame[cnt][i])
            visited[i] = False

for ts in range(1, t+1):
    n = int(input())
    frame = [[] for _ in range(n)]
    min = 2147000000

    for i in range(n):
        frame[i] = list(map(int, input().split()))

    res = [0] * n
    idx = list(range(n))
    visited = [False] * (n)

    powset(0, 0)

    print('#%d'%ts, min)