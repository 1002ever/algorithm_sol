frame = [[] for _ in range(9)]
chkp = []
state_chk = 0

for i in range(9):
    frame[i] = list(map(int, input().split()))
    if frame[i].count(0) == 1:
        frame[i][frame[i].index(0)] = 45 - sum(frame[i])
    elif frame[i].count(0) > 1:
        for j in range(9):
            if frame[i][j] == 0:
                chkp.append((i,j))

while 1:
    cnt = 0
    state_chk = (state_chk + 1) % 2 # 1이면 행렬 바뀐 상태
    frame = list(map(list,zip(*frame)))
    for i in range(9):
        if frame[i].count(0) == 1:
            cnt += 1
            j = frame[i].index(0)
            frame[i][frame[i].index(0)] = 45 - sum(frame[i])

            if state_chk == 0:
                chkp.remove((i,j))
            else:
                chkp.remove((j,i))

    for i in range(9):
        tmpsum = 0
        tmpcnt = 0
        tmpxy = []
        for j in range(3):
            j = (i%3)*3+j
            for k in range(3):
                k = k + (i//3)*3
                if frame[j][k] == 0:
                    tmpcnt += 1
                    tmpxy.append((j,k))
                tmpsum += frame[j][k]
        if tmpcnt == 1:
            cnt += 1
            x, y = tmpxy.pop()
            frame[x][y] = 45 - tmpsum
            if state_chk == 0:
                chkp.remove((x,y))
            else:
                chkp.remove((y,x))

    if cnt == 0:
        break

if state_chk == 1:
    frame = list(zip(*frame))
print(frame)