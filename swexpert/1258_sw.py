from collections import deque

dx = [1, 0]
dy = [0, 1]

def multi(a):
    return a[0]*a[1]


def bfs(x, y):
    r_x = x
    c_y = y
    rcnt = 1
    lcnt = 1

    while 1:
        r_x += 1
        if not (0 <= r_x < n):
            break
        if frame[r_x][y] > 0:
            rcnt += 1
        else:
            break
    while 1:
        c_y += 1
        if not (0 <= c_y < n):
            break
        if frame[x][c_y] > 0:
            lcnt += 1
        else:
            break

    for i in range(x, x+rcnt):
        for j in range(y, y+lcnt):
            visited[i][j] = True

    return((rcnt, lcnt))

t = int(input())

for ts in range(1, t+1):
    n = int(input())
    frame = [[] for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    matrix_list = []
    for i in range(n):
        frame[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            if frame[i][j] > 0 and visited[i][j] == False:
                cnt += 1
                matrix_list.append(bfs(i,j))

    matrix_list = sorted(matrix_list, key=lambda x : (multi(x),x[0]))

    print('#%d'%ts, cnt, end=' ')
    for i in range(len(matrix_list)):
        print(matrix_list[i][0], matrix_list[i][1], end=' ')
    print('')
