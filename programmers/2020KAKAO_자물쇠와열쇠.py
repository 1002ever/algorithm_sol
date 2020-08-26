def turn(frame, m):
    temp = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            temp[i][j] = frame[m-j-1][i]
    return temp

def solution(key, lock):
    key_set = []
    m = len(key)
    n = len(lock)
    key_set.append(turn(key, m))

    for i in range(3):
        key_set.append(turn(key_set[-1], m))
        
    
    chk_frame_len = n+(2*m)-2
    for z in range(4):

        for i in range(chk_frame_len-m+1):
            for j in range(chk_frame_len-m+1):
                
                # Lock을 가운데 놓은 판별 위한 판 마련
                chk_frame = [[0]*(n+(2*m)-2) for _ in range(n+(2*m)-2)]
                for a in range(n):
                    for b in range(n):
                        chk_frame[a+m-1] [b+m-1] = lock[a][b]
                
                false_chk = 0
                for k in range(m):
                    for l in range(m):
                        chk_frame[i+k][j+l] += key_set[z][k][l]
                
                for k in range(n):
                    for l in range(n):
                        if chk_frame[m-1+k][m-1+l] != 1:
                            false_chk = 1
                            break
                    if false_chk == 1:
                        break
                if false_chk == 1:
                    continue
                    
                return 1
            
    return 0