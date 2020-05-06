# 하-우 순
dx = [1, 0]
dy = [0, 1]

def dfs(x, y, fsum):
    global ans
    # 더하다가 ans보다 커지면 중지
    if fsum > ans:
        return

    if (x, y) == (n-1, n-1):
        if ans > fsum:
            ans = fsum 
        return

    for i in range(2):
        mx = x+dx[i]
        my = y+dy[i]
        if 0<=mx<n and 0<=my<n:
            dfs(mx, my, fsum+frame[mx][my])

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    frame = [[] for _ in range(n)]
    ans = 2147000000
    for i in range(n):
        frame[i] = list(map(int, input().split()))
    dfs(0, 0, frame[0][0])
    print("#%d"%tc, ans)