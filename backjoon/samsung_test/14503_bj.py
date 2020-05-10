# 삼성 코테 기출 - 백준 14503(로봇 청소기)

# 북서남동 순
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, d):
    global ans
    
    if frame[x][y] == 0:
        frame[x][y] = 2
        ans += 1

    for i in range(d+1, d+5):
        i = i % 4
        mx = x + dx[i]
        my = y + dy[i]
        if frame[mx][my] == 0:
            dfs(mx, my, i)
            return
    
    # 후진 기어
    mx = x - dx[d]
    my = y - dy[d]
    if frame[mx][my] == 1:
        return
    else:
        dfs(mx, my, d)
        
n, m = map(int, input().split())
# d = 0123 북동남서순
x, y, d = map(int, input().split())
frame = [[] for _ in range(n)]
ans = 0

# 내가 설정한 좌표계로 d 값 변경
if d == 1:
    d = 3
elif d == 3:
    d = 1
for i in range(n):
    frame[i] = list(map(int, input().split()))

dfs(x, y, d)
print(ans)