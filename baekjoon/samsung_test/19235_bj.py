# 백준 19235 모노미노도미노 - 삼성 코테 기출

n = int(input())
green = [[0]*4 for _ in range(6)]
# 행열 바뀐 꼴로 생각한다면
blue = [[0]*4 for _ in range(6)]

ans1 = 0
ans2 = 0

def block_down(color, frame, t, x, y, i):
    if color == 'green':
        mx, my = 1, y
    else:
        mx, my = 1, x

    # 한 칸씩만 검사 필요한 경우
    if (color == 'green' and (t == 1 or t == 3)) or (color == 'blue' and (t == 1 or t == 2)):
        chk = 0
        while frame[mx+1][my] == 0:
            chk = 1
            mx += 1
            if mx == 5:
                break
        if chk == 0:
            return frame
        if color == 'green':
            frame[1][y] = 0
        else:
            frame[1][x] = 0
        frame[mx][my] = i
        if (color == 'green' and t == 3):
            frame[0][y] = 0
            frame[mx-1][my] = i
        if (color == 'blue' and t == 2):
            frame[0][x] = 0
            frame[mx-1][my] = i
    # 두 칸씩 검사 필요한 경우
    else:
        chk = 0
        while frame[mx+1][my] == 0 and frame[mx+1][my+1] == 0:
            chk = 1
            mx += 1
            if mx == 5:
                break
        if chk == 0:
            return frame
        frame[1][my] = 0
        frame[1][my+1] = 0
        frame[mx][my] = i
        frame[mx][my+1] = i

    return frame

def erase_line(frame):
    global ans1

    chk = 0
    for i in range(5, -1, -1):
        if frame[i].count(0) == 0:
            ans1 += 1
            chk = 1
            for j in range(4):
                frame[i][j] = 0
    return [frame, chk]

def erase_block_down(frame):
    idx = 4
    visited = [[0]*4 for _ in range(6)]
    while idx >= 0:
        chk = 0
        for i in range(4):
            if frame[idx][i] == 0:
                continue
            if i < 3 and frame[idx][i+1] == frame[idx][i]:
                bnum = 2
            elif idx > 0 and frame[idx-1][i] == frame[idx][i]:
                bnum = 3
            elif (idx > 0 and frame[idx][i-1] == frame[idx][i]) or (frame[idx][i] == frame[idx+1][i]):
                continue
            else:
                bnum = 1
            
            if bnum == 1 or bnum == 3:
                mx, my = idx, i
                while frame[mx+1][my] == 0:
                    chk = 1
                    mx += 1
                    if mx == 5:
                        break
                if chk == 1:
                    z = frame[idx][i]
                    frame[idx][i] = 0
                    frame[mx][my] = z
                    if bnum == 3:
                        frame[idx-1][i] = 0
                        frame[mx-1][my] = z
            else:
                mx, my = idx, i
                while frame[mx+1][my] == 0 and frame[mx+1][my+1] == 0:
                    chk = 1
                    mx += 1
                    if mx == 5:
                        break
                if chk == 1:
                    z = frame[idx][i]
                    frame[idx][i] = 0
                    frame[idx][i+1] = 0
                    frame[mx][my] = z
                    frame[mx][my+1] = z

            if chk == 1:
                break
        if chk == 0:
            idx -= 1

    return frame

def push_white(frame):
    if frame[1].count(0) < 4:
        for i in range(5, 0, -1):
            frame[i] = frame[i-1][:]
        for i in range(4):
            frame[0][i] = 0
    if frame[1].count(0) < 4:
        for i in range(5, 1, -1):
            frame[i] = frame[i-1][:]
        for i in range(4):
            frame[1][i] = 0
    return frame


for i in range(1, n+1):
    t, x, y = map(int, input().split())
    # 블럭을 일단 연한 공간에 쌓기
    if t == 1:
        green[1][y] = i
        blue[1][x] = i
    elif t == 2:
        green[1][y] = i
        green[1][y+1] = i
        blue[0][x] = i
        blue[1][x] = i
    else:
        green[0][y] = i
        green[1][y] = i
        blue[1][x] = i
        blue[1][x+1] = i

    # 1. 블럭 내리기
    green = block_down('green', green, t, x, y, i)
    blue = block_down('blue', blue, t, x, y, i)

    # print('블록 내리고')
    # print(green)
    # print(blue)

    while 1:
        # 2. 블럭 상쇄
        green, chk1 = erase_line(green)
        blue, chk2 = erase_line(blue)
        if chk1 == 0 and chk2 == 0:
            break
        # 3. 블럭 상쇄된 것 내리기
        if chk1 == 1:
            green = erase_block_down(green)
        if chk2 == 1:
            blue = erase_block_down(blue)

    # print('블록 상쇄 후')
    # print(green)
    # print(blue)

    # 4. 연한 공간 처리
    green = push_white(green)
    blue = push_white(blue)

    # print('다 처리 후')
    # print(green)
    # print(blue)

for i in range(6):
    for j in range(4):
        if green[i][j] != 0:
            ans2 += 1
        if blue[i][j] != 0:
            ans2 += 1

print(ans1)
print(ans2)