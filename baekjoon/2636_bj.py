from collections import deque

dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]

def bfs(x, y):
    q.appendleft((x,y))
    while q:
        x, y = q.pop()
        for i in range(4):
            m_x = x+dx[i]
            m_y = y+dy[i]
            if 0 <= m_x < m and 0 <= m_y < n:
                if frame[m_x][m_y] == 0 and visited[m_x][m_y] == False:
                    visited[m_x][m_y] = True
                    q.appendleft((m_x, m_y))
                if frame[m_x][m_y] == 1 and chk[m_x][m_y] == 0:
                    chk[m_x][m_y] = 1
    for i in range(m):
        for j in range(n):
            if chk[i][j] == 1:
                frame[i][j] -= 1
    sumf = 0
    for i in range(m):
        sumf += sum(frame[i])
    return sumf

m, n = map(int, input().split())
frame = [[] for _ in range(m)]
q = deque()
ans_list = []
ans = 1 # 의미없는 초기값
cnt = 0
ss = 0

for i in range(m):
    frame[i] = list(map(int, input().split()))
    ss += sum(frame[i])

ans_list.append(ss)

while ans != 0:
    cnt += 1
    visited = [[False]*n for _ in range(m)]
    chk = [[0]*n for _ in range(m)]
    ans = bfs(0,0)
    ans_list.append(ans)

print(cnt)
print(ans_list[-2])