t = int(input())

for ts in range(1, t+1):
    n = int(input())
    frame = [[] for _ in range(n)]
    ans = 0

    for i in range(n):
        frame[i] = list(map(int, list(input())))

    c = int((n-1)/2)+1
    num = -1
    for i in range(n):
        if i <= int(n/2):
            c -= 1
            num += 2
            for j in range(num):
                ans += frame[i][c+j]

        else:
            c += 1
            num -= 2
            for j in range(num):
                ans += frame[i][c+j]

    print('#%d'%ts, ans)