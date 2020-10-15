# 백준 16234 인구이동 - 삼성 코테 기출
from collections import deque


class Union:
    def __init__(self, union, pop_sum):
        self.union = union
        self.pop_sum = pop_sum

def search_xy():
    global ans
    global visited

    chk = 0
    union_num = 1
    union_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                union = bfs(i, j, union_num)
                if union != 0:
                    chk = 1
                    union_list.append(union)
                union_num += 1

    if chk == 1:
        ans += 1
        visited = [[0]*n for _ in range(n)]
        for i in range(len(union_list)):
            union_sum = union_list[i].pop_sum
            union_len = len(union_list[i].union)
            pop = union_sum // union_len
            for j in range(union_len):
                x, y = union_list[i].union.pop()
                frame[x][y] = pop

    return chk

def bfs(x, y, union_num):
    
    global ans
    global visited

    q = deque()
    q.appendleft((x, y))
    visited[x][y] = union_num
    union = [(x, y)]
    pop_sum = frame[x][y]

    while q:
        x, y = q.pop()
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            if visited[mx][my] == 0 and abs(frame[mx][my] - frame[x][y]) >= l and abs(frame[mx][my] - frame[x][y]) <= r:
                q.appendleft((mx, my))
                visited[mx][my] = union_num
                union.append((mx, my))
                pop_sum += frame[mx][my]
    
    if len(union) > 1:
        return Union(union, pop_sum)
    else:
        return 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
frame = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = 0

for i in range(n):
    frame[i] = list(map(int, input().split()))

chk = 1
while chk == 1:
    chk = search_xy()

print(ans)