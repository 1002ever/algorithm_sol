def turn(frame, m):
    temp = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            print(i, j, m-j, i)
            temp[i][j] = frame[m-j-1][i]
    return temp

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

key_set = []
m = len(key)
n = len(lock)

key_set.append(turn(key, m))

for i in range(3):
    key_set.append(turn(key_set[-1], m))
    
print(key_set)

