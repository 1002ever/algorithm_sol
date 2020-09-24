def r_com(frame):
    max_len = len(frame[0])
    temp_frame = []

    for i in range(len(frame)):
        temp_row = []
        for j in range(len(frame[i])):
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
            for j in range(max_len - len(temp_frame[i])):
                temp_frame[i].append([0,0])

    frame = [[0]*(max_len*2) for _ in range(len(temp_frame))]
    for i in range(len(temp_frame)):
        idx = 0
        for j in range(max_len):
            for k in range(2):
               frame[i][idx] = temp_frame[i][j][k]
    print(frame)

def c_com(frame):
    pass

r, c, k = map(int, input().split())
frame = [ [] for _ in range(3) ]
for i in range(3):
    frame[i] = list(map(int, input().split()))

sec = 0
while frame[r][c] != k:
    sec += 1
    if len(frame) >= len(frame[0]):
        frame = r_com(frame)
        break
    else:
        frame = c_com(frame)