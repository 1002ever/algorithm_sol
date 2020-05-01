# 백준 12100 삼성 코테 문제집, 2048(Easy)

def turn(frame):
    turn_frame = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turn_frame[i][j] = frame[j][n-i-1]
    return turn_frame

def move(frame):
    move_frame = [[] for _ in range(n)]
    for i in range(n):
        temp_list = []
        addchk = 0
        for j in range(n):
            if frame[i][j] == 0:
                continue

            if len(temp_list) == 0:
                temp_list.append(frame[i][j])
            elif frame[i][j] == temp_list[-1] and addchk != 1:
                temp_list[-1] = temp_list[-1]*2
                addchk = 1
            else:
                temp_list.append(frame[i][j])
                addchk = 0
        for k in range(n-len(temp_list)):
            temp_list.append(0)
        move_frame[i] = temp_list
    return move_frame

def maxchk(frame):
    maxn = -2147000000
    for i in range(n):
        for j in range(n):
            if frame[i][j] > maxn:
                maxn = frame[i][j]
    return maxn

def dfs(frame, cnt):
    global ans
    if cnt == 5:
        temp_max = maxchk(frame)
        if ans < temp_max:
            ans = temp_max
        return
    for i in range(4):
        temp_frame = turn(frame)
        frame = temp_frame
        temp_frame = move(temp_frame)
        dfs(temp_frame, cnt+1)
    
n = int(input())
ans = -2147000000
frame = [[] for _ in range(n)]

for i in range(n):
    frame[i] = list(map(int, input().split()))

dfs(frame, 0)
print(ans)