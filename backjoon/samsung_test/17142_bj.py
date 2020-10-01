# 백준 17142 연구소2 - 삼성 코테 기출

from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dispose(frame, virus_case, zero_cnt):
    sec = 0
    q = deque()
    for (x, y) in virus_case:
        q.appendleft((x, y))
        frame[x][y] = 3
    
    while q:
        sec += 1
        # 예전에 기록된 시간보다 더 오래걸린다면
        if sec >= min_sec:
            return 2147000000
        for i in range(len(q)):
            x, y = q.pop()
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                # 프레임 밖
                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue
                # 벽이나 이미 활성화된 바이러스 만났을 때
                if frame[mx][my] == 1 or frame[mx][my] == 3:
                    continue
                else:
                    if frame[mx][my] == 0:
                        zero_cnt -= 1
                        if zero_cnt == 0:
                            return sec
                    frame[mx][my] = 3
                    q.appendleft((mx, my))
        
    if zero_cnt > 0:
        return 2147000000
    return sec
            
    

n, m = map(int, input().split())
frame = [[] for _ in range(n)]
virus_pos = deque()
zero_cnt = 0
min_sec = 2147000000

for i in range(n):
    frame[i] = list(map(int, input().split()))
    zero_cnt += frame[i].count(0)
    for j in range(n):
        if frame[i][j] == 2:
            virus_pos.appendleft((i, j))

# 감염 시작 전 검사
if zero_cnt == 0:
    min_sec = 0

if min_sec != 0:
    for virus_case in combinations(virus_pos, m):
        tmp_frame = [[] for _ in range(n)]
        for i in range(n):
            tmp_frame[i] = frame[i][:]
        cur_sec = dispose(tmp_frame, virus_case, zero_cnt)
        if min_sec > cur_sec:
            min_sec = cur_sec

if min_sec == 2147000000:
    print(-1)
else:
    print(min_sec)
# (0, 0), (1, 5), (4, 3) 일 떄 최소