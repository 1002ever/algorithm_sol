T = int(input())

for ts in range(1, T+1):
    chars = input()
    leng = len(chars)
    frame_leng = leng + 4 +(3*(leng-1))
    frame = [['.']*frame_leng for _ in range(5)]
    
    for i in range(5):
        if i == 0 or i == 4:
            for j in range(2, frame_leng, 4):
                frame[i][j] = '#'
        elif i == 1 or i == 3:
            for k in range(1, frame_leng, 2):
                frame[i][k] = '#'
        else:
            for l in range(0, frame_leng, 4):
                frame[i][l] = '#'

    for m in range(leng):           
        frame[2][2+(4*m)]= chars[m]
    
    for n in range(5):
        print(''.join(frame[n]))
