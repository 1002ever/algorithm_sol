from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chkmov(i, m_x, m_y):
    tmp = chkpoint(frame[m_x][m_y])
    if i == 0:
        chk_m = 1
    elif i == 1:
        chk_m = 0
    elif i == 2:
        chk_m = 3
    elif i == 3:
        chk_m = 2
    else:
        chk_m = -1

    if chk_m in tmp:
        return True
    else:
        return False

def chkpoint(idx):
    if idx == 1:
        return [0,1,2,3]
    elif idx == 2:
        return [0,1]
    elif idx == 3:
        return [2,3]
    elif idx == 4:
        return [0,3]
    elif idx == 5:
        return [1,3]
    elif idx == 6:
        return [1,2]
    else:
        return [0,2]

def bfs(x, y):
    global cnt
    stage = 1
    q = deque()
    visited[x][y] = True
    q.appendleft((x, y))

    while q:
        stage += 1
        if stage > l:
            break
        for i in range(len(q)):
            x, y = q.pop()
            chk_p = chkpoint(frame[x][y])
            for i in range(4): # 좌 우 상 하
                if i in chk_p:
                    m_x = x+dx[i]
                    m_y = y+dy[i]
                    if 0 <= m_x < n and 0 <= m_y < m:
                        if frame[m_x][m_y] > 0 and visited[m_x][m_y] == False and chkmov(i, m_x, m_y):
                            cnt += 1
                            visited[m_x][m_y] = True
                            q.appendleft((m_x, m_y))

t = int(input())
for ts in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    cnt = 1
    frame = [[] for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        frame[i] = list(map(int, input().split()))

    bfs(r, c)

    print('#%d'%ts, cnt)