T = int(input())

for tc in range(1, T+1):
    print('#%d'%tc, end=' ')
    frame= [[] for _ in range(9)]
    err = 0

    for i in range(9):
        frame[i] = list(map(int, input().split()))

    for j in range(9):
        x = (j // 3) * 3
        y = (j % 3) * 3
        square_sum = 0
        col_sum = 0

        if sum(frame[j]) != 45:
            print(0)
            err = 1
            break
        
        mx = x
        my = y
        for k in range(9):
            square_sum += frame[mx][my]
            if (k%3) == 2:
                mx += 1
                my = y
            else:
                my += 1
        if square_sum != 45:
            print(0)
            err = 1
            break

        for l in range(9):
            col_sum += frame[l][j]
        if col_sum != 45:
            print(0)
            err = 1
            break

    if err != 1:
        print(1)