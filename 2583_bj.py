from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.appendleft((x,y))
    cnt = 0
    while q:
        x, y = q.pop()
        cnt += 1
        for i in range(4):
            m_x = x+dx[i]
            m_y = y+dy[i]
            if 0 <= m_x < m and 0 <= m_y < n:
                if visited[m_x][m_y] == False and frame[m_x][m_y] == 0:
                    visited[m_x][m_y] = True
                    q.appendleft((m_x, m_y))

    return cnt

m, n, k = map(int, input().split())

frame = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
cnt_list = []

for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            frame[x][y] += 1


for i in range(m):
    for j in range(n):
        if visited[i][j]== False and frame[i][j] == 0:
            cnt_list.append(bfs(i,j))

cnt_list.sort()

print(len(cnt_list))
for i in range(len(cnt_list)):
    print(cnt_list[i], end=' ')