# 삼성 A형 테스트 기출 - 17070 파이프 옮기기 1

from collections import deque

# 0 가로, 1 아래 대각, 2 아래 
dx = [0, 1, 1]
dy = [1, 1, 0]

n = int(input())
frame = [[] for _ in range(n)]
# 가로로 시작
ans = 0

for i in range(n):
    frame[i] = list(map(int, input().split()))

# 0일 땐 0, 1만 가능
# 1일 땐 0, 1, 2 다 가능
# 2일 땐 1, 2만 가능

q = deque()
q.appendleft([0, 1, 0])

while q:
    x, y, dir = q.pop()
    if x == n-1 and y == n-1:
        ans += 1
        continue
    for i in range(3):
        if dir == 0 and i == 2:
            continue
        if dir == 2 and i == 0:
            continue
        
        if i == 1:
            if x+1 >= n or y+1 >= n:
                continue
            if frame[x+1][y] != 0 or frame[x+1][y+1] != 0 or frame[x][y+1] != 0:
                continue
            q.appendleft([x+1, y+1, 1])
        else:
            mx = x + dx[i]
            my = y + dy[i]
            if mx >= n or my >= n:
                continue
            if frame[mx][my] != 0:
                continue
            q.appendleft([mx, my, i])

print(ans)