# 삼성 역테 기출 (백준 15686 - 치킨 배달)
# 장애물 없다는 점을 까먹고 bfs로 삽질했지만..
# 좌표로 단순 반복으로 계산하니 가볍게 통과

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def mind_chk(ck_m):
    global ans

    local_min = 0
    
    for i in range(len(home_xy)):
        temp = 2147000000
        for j in range(len(ck_m)):
            temp2 = abs(home_xy[i][0] - ck_m[j][0]) + abs(home_xy[i][1] - ck_m[j][1])
            if temp2 < temp:
                temp = temp2
        local_min += temp

    if ans > local_min:
        ans = local_min

def comb(ck_m, idx, cnt):
    if cnt == m:
        mind_chk(ck_m)
    else:
        for i in range(idx, len(ck_xy)):
            ck_m.append(ck_xy[i])
            comb(ck_m, i+1, cnt+1)
            ck_m.pop()

n, m = map(int, input().split())
home_xy = []
ck_xy = []
frame = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = 2147000000

for i in range(n):
    frame[i] = list(map(int, input().split()))
    for j in range(n):
        if frame[i][j] == 0:
            continue
        elif frame[i][j] == 1:
            home_xy.append((i, j))
        else:
            ck_xy.append((i, j))

comb([], 0, 0)
print(ans)