# 백준 18428 감시 피하기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_std(wall_list):
    for teacher in teachers:
        x, y = teacher
        for i in range(4):
            mx, my = x, y
            while 1:
                mx = mx + dx[i]
                my = my + dy[i]
                # range 초과
                if mx < 0 or mx >= n or my < 0 or my >= n:
                    break
                # 벽 만나면 break
                if frame[mx][my] == 'wall':
                    break
                # 학생 만나면 False
                if frame[mx][my] == 'S':
                    return False
    return True
                

def comb_walls(cnt, x, y, wall_list):
    global ans

    if ans == "YES":
        return

    if cnt == 3:
        # 벽 세우기
        for i in range(3):
            x, y = wall_list[i]
            frame[x][y] = 'wall'
        if chk_std(wall_list):
            ans = "YES"
        for i in range(3):
            x, y = wall_list[i]
            frame[x][y] = 'X'
        return

    if y >= n:
        y = 0
        x += 1
     
    for i in range(x, n):
        for j in range(y, n):
            if frame[i][j] == 'X':
                wall_list.append((i, j))
                comb_walls(cnt+1, i, j+1, wall_list)
                wall_list.pop()
            
            if j == n-1:
                y = 0
                

ans = "NO"
cntcnt = 0
n = int(input())
frame = [[] for _ in range(n)]
teachers = []
for i in range(n):
    frame[i] = input().split()
    for j in range(n):
        if frame[i][j] == 'T':
            teachers.append([i,j])

comb_walls(0, 0, 0, [])
print(ans)