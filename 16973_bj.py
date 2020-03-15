from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    q = deque()
    visited.add((x,y))
    q.appendleft((x, y))
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.pop()
            if (x, y) == (fr, fc):
                return cnt
            for i in range(4):
                m_x = x + dx[i]
                m_y = y + dy[i]
                if (m_x, m_y) in visited:
                    continue
                if 0 < m_x <= (n-h+1) and 0 < m_y <= (m-w+1):
                    temp_sum = 0
                    for j in range(h):
                        temp_sum += sum(frame[m_x+j][m_y:m_y+w])
                        if temp_sum != 0:
                            break
                    if temp_sum == 0:
                        visited.add((m_x, m_y))
                        q.appendleft((m_x, m_y))
    return -1

n, m = map(int, input().split())
frame = [[0] for _ in range(n+1)]
visited = set()
cnt = -1

for i in range(0, n+1):
    if i == 0:
        frame[i] = frame[i] + [0]*m
        continue
    tmp_list = list(map(int, input().split()))
    frame[i] = frame[i] + tmp_list
h, w, sr, sc, fr, fc = map(int, input().split())

print(bfs(sr, sc))