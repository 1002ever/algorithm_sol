# 삼성 A형 테스트 기출 - 17135 캐슬 디펜스

from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -2147000000
tmp_ans = 0

def endChk(frame, n):
    tmp_sum = 0
    for i in range(n):
        tmp_sum += sum(frame[i])
        if tmp_sum > 0:
            return True
    return False

def bfs(frame, xy, d):
    global tmp_ans

    q = deque()
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    x, y = xy
    q.appendleft((x, y))

    cand_xy = []
    while cnt < d and q:
        cnt += 1
        x, y = q.pop()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            if visited[mx][my] == 1:
                continue
            if frame[mx][my] == 1:
                cand_xy.append((mx, my))
            q.appendleft((mx, my))
            visited[mx][my] = 1
        if cand_xy:
            break
    if len(cand_xy) == 1:
        return cand_xy[0]
    elif len(cand_xy) > 1:
        cand_xy = sorted(cand_xy, key = lambda x : x[1])
        return cand_xy[0]
    else:
        return -1

def dfs(frame, cand, d, n, m):
    global ans
    global tmp_ans

    tmp_ans = 0
    while endChk(frame, n):
        del_xy = []
        for y in cand:
            xy = [n, y]
            del_xy.append(bfs(frame, xy, d))
        for xy in del_xy:
            if xy == -1:
                continue
            else:
                x, y = xy
                frame[x][y] = 0
                tmp_ans += 1
        # 아래로 이동
        for i in range(n):
            for j in range(m):
                if frame[i][j] == 1:
                    frame[i][j] = 0
                    if i != n-1:
                        frame[i+1][j] = 1
        
        print(frame)

    if tmp_ans > ans:
        ans = tmp_ans
    
n, m, d = map(int, input().split())
frame = [[] for _ in range(n+1)]
frame[n] = [0]*m
for i in range(n):
    frame[i] = list(map(int, input().split()))

cand_y = range(m)
for cand in combinations(cand_y, 3):
    dfs(frame, list(cand), d, n, m)

print(ans)