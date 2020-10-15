# 백준 13460 구슬 탈출 2

from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# rst, bst는 공의 상태를 암시
# 1이면 정지 상태, rst가 O에 들어가면 2, bst가 O에 들어가면 끝이므로 return
# 공이 겹치면 더 많이 움직인 것을 한 칸 빼준다.
def move(rx, ry, bx, by, i):
    rst, bst = 0, 0
    rcnt, bcnt = 0, 0

    while 1:
        mrx = rx + dx[i]
        mry = ry + dy[i]
        if frame[mrx][mry] == '#':
            rst = 1
        elif frame[mrx][mry] == 'O':
            rst = 2
        else:
            rst = 0
            rcnt += 1
            rx = mrx
            ry = mry

        mbx = bx + dx[i]
        mby = by + dy[i]
        if frame[mbx][mby] == '#':
            bst = 1
        elif frame[mbx][mby] == 'O':
            bst = 2
            return((-1, -1, -1, -1))
        else:
            bst = 0
            bcnt += 1
            bx = mbx
            by = mby
        
        if rst == 1 and bst == 1:
            if (rx, ry) == (bx ,by):
                if rcnt > bcnt:
                    rx = rx - dx[i]
                    ry = ry - dy[i]
                else:
                    bx = bx - dx[i]
                    by = by - dy[i]
            return((rx, ry, bx, by))
        elif rst == 2 and bst == 1:
            return((-2, -2, -2, -2))

# move 함수의 결과로 탐색 진행.
# visited 를 활용하여 탐색 지점을 줄여준다.
def bfs(rx, ry, bx, by):
    q = deque()
    visited.add((rx, ry, bx, by))
    q.append((rx, ry, bx, by))
    cnt = 0
    while q:
        cnt += 1
        if cnt > 10:
            return -1
        for z in range(len(q)):
            rx, ry, bx, by = q.popleft()
            for i in range(4):
                mrx, mry, mbx, mby = move(rx, ry, bx, by, i)
                if (mrx, mry, mbx, mby) == (-2, -2, -2, -2):
                    return cnt
                elif (mrx, mry, mbx, mby) != (-1, -1, -1, -1):
                    if (mrx, mry, mbx, mby) not in visited:
                        visited.add((mrx, mry, mbx, mby))
                        q.append((mrx, mry, mbx, mby))
    return -1



n, m = map(int, input().split())
frame = [[] for _ in range(n)]
visited = set()

for i in range(n):
    frame[i] = list(input())

for i in range(1, n-1):
    for j in range(1, m-1):
        if frame[i][j] != '.':
            if frame[i][j] == 'R':
                rx, ry = i, j
            elif frame[i][j] == 'B':
                bx, by = i, j

ans = bfs(rx, ry, bx, by)
print(ans)