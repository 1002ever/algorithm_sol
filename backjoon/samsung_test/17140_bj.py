# 삼성 코테 대비 - 백준 17140

def r_com(frame):
    max_len = 1.5
    temp_frame = []

    for i in range(len(frame)):
        temp_row = []
        for j in range(len(frame[i])):
            if frame[i][j] == 0:
                continue
            if temp_row.count([frame[i][j], frame[i].count(frame[i][j])]) > 0:
                pass
            else:
                temp_row.append([frame[i][j], frame[i].count(frame[i][j])])
        temp_row = sorted(temp_row, key = lambda x : (x[1], x[0]))
        if len(temp_row) > max_len:
            max_len = len(temp_row)
        temp_frame.append(temp_row)
        
    for i in range(len(temp_frame)):
        if len(temp_frame[i]) < max_len:
            for j in range(int(max_len) - len(temp_frame[i])):
                temp_frame[i].append([0,0])

    frame = [[0]*int(max_len*2) for _ in range(len(temp_frame))]
    for i in range(len(temp_frame)):
        idx = 0
        for j in range(int(max_len)):
            for k in range(2):
                frame[i][idx] = temp_frame[i][j][k]
                idx += 1
            if idx >= 100:
                break
    return frame

def c_com(frame):
    frame = [list(x) for x in zip(*frame)]
    frame = r_com(frame)
    frame = [list(x) for x in zip(*frame)]
    return frame

r, c, k = map(int, input().split())
frame = [ [] for _ in range(3) ]
for i in range(3):
    frame[i] = list(map(int, input().split()))

sec = 0
while 1:
    try:
        if frame[r-1][c-1] == k:
            break
        sec += 1
        if sec > 100:
            sec = -1
            break
        if len(frame) >= len(frame[0]):
            frame = r_com(frame)
        else:
            frame = c_com(frame)
    except:
        sec += 1
        if sec > 100:
            sec = -1
            break
        if len(frame) >= len(frame[0]):
            frame = r_com(frame)
        else:
            frame = c_com(frame)
        

print(sec)