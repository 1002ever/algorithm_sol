dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global path
    global path_list

    if cnt == 7:
        path_list.add(path)
        return

    else:
        for i in range(4):
            m_x = x + dx[i]
            m_y = y + dy[i]
            if 0 <= m_x < 4 and 0 <= m_y < 4:
                path = path + str(frame[m_x][m_y])
                dfs(m_x, m_y, cnt+1)
                path = path[0:len(path)-1]

t = int(input())

for ts in range(1, t+1):
    frame = [[] for _ in range(4)]
    path = ''
    path_list = set()
    for i in range(4):
        frame[i] = list(map(int, input().split()))

    for i in range(4):
        for j in range(4):
            path = str(frame[i][j])
            dfs(i,j,1)
    print('#%d'%ts, len(path_list))