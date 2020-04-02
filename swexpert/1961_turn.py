def turn(matrix):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = str(matrix[N-1-j][i])
    return temp

T = int(input())

for ts in range(1, T+1):
    N = int(input())
    mat = [[] for _ in range(N)]
    for i in range(N):
        mat[i] = list(map(int, input().split()))
        
    mat90 = turn(mat)
    mat180 = turn(mat90)
    mat270 = turn(mat180)

    print('#%d'%ts)
    
    for j in range(N):
        print(''.join(mat90[j]), end=' ')
        print(''.join(mat180[j]), end=' ')
        print(''.join(mat270[j]), end=' ')
        print()




