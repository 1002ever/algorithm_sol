# 백준 삼성 역테 기출 ( 백준 15685 - 드래곤커브)

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n = int(input())

def chk_square(y, x):
    if frame[y][x] == 1 and frame[y+1][x] == 1 and frame[y][x+1] == 1 and frame[y+1][x+1] == 1:
        return True
    return False

def turn(cur_d):
    if cur_d == 0:
        return 1
    elif cur_d == 1:
        return 2
    elif cur_d == 2:
        return 3
    else:
        return 0

def make_curve(trace, stage):
    if stage == cur_curve[3]:
        return trace
    else:
        if trace == []:
            trace.append(cur_curve[2])
        else:
            temp = trace[:]
            for i in range(len(temp)):
                cur_d = temp[-i-1]
                trace.append(turn(cur_d))
        return make_curve(trace, stage+1)

frame = [[0]*101 for _ in range(101)]
curves = []
ans = 0

for i in range(n):
    cur_curve = list(map(int, input().split()))
    curves.append(cur_curve)
    trace = make_curve([], -1)
    
    cur_x = cur_curve[0]
    cur_y = cur_curve[1]
    frame[cur_y][cur_x] = 1

    for j in trace:
        cur_x = cur_x + dx[j]
        cur_y = cur_y + dy[j]
        frame[cur_y][cur_x] = 1

for i in range(100):
    for j in range(100):
        if frame[i][j] == 1:
            if chk_square(i, j):
                ans += 1

print(ans)