# 백준 16236 아기 상어 - 삼성 코테 기출
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
size = 2
exp = 0
ans = 0

frame = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def find_fish(x, y):
    global exp
    global size
    global ans

    q = deque()
    q.appendleft((x, y))
    visited[x][y] = 1
    sec = 0
    candidate = []

    while q:
        sec += 1
        for z in range(len(q)):
            xx, yy = q.pop()
            for i in range(4):
                mx = xx+dx[i]
                my = yy+dy[i]

                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue

                if visited[mx][my] == 0 and frame[mx][my] <= size:
                    q.appendleft((mx, my))
                    visited[mx][my] = 1

                    # 잡아먹을 수 있음?
                    if 1 <= frame[mx][my] < size:
                        # 같은 level 내에 잡아먹을 수 있는거 있음?
                        if candidate:
                            # 있다면 행 비교
                            if candidate[0] > mx:
                                candidate = [mx, my]
                            # 행도 같다면 열 비교
                            elif candidate[0] == mx and candidate[1] > my:
                                candidate = [mx, my]
                        # 같은 level 내 없었다면 새로 추가
                        else:
                            candidate = [mx, my]

        if candidate:
            exp += 1
            ans += sec
            frame[x][y] = 0
            if exp == size:
                size += 1
                exp = 0
            return (0, candidate[0], candidate[1])
    return (1, 0, 0)

x, y = 0, 0
for i in range(n):
    frame[i] = list(map(int, input().split()))
    if 9 in frame[i]:
        x, y = i, frame[i].index(9)

chk = 0
while chk == 0:
    visited = [[0]*n for _ in range(n)]
    chk, x, y = find_fish(x, y)

print(ans)