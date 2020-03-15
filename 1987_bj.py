dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global max_ans
    trace_alpha.append((x,y))
    print(trace_alpha)

    mc = 0
    for i in range(4):
        m_x = x + dx[i]
        m_y = y + dy[i]
        if 0 <= m_x < r and 0 <= m_y < c:
            if visited_alpha[ord(frame[m_x][m_y])-65] == 0:
                mc = 1
                visited_alpha[ord(frame[m_x][m_y])-65] += 1
                dfs(m_x, m_y, cnt+1)
                trace_alpha.remove((m_x,m_y))
                visited_alpha[ord(frame[m_x][m_y])-65] -= 1

    if mc == 0:
        print(cnt)
        if cnt > max_ans:
            max_ans = cnt
        return

r, c = map(int, input().split())
frame = [[] for _ in range(r)]
visited_alpha = [0]*26
max_ans = -2147000000
trace_alpha = []

for i in range(r):
    frame[i] = input()

visited_alpha[ord(frame[0][0])-65] += 1
dfs(0, 0, 1)
print(max_ans)