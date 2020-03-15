t = int(input())

for ts in range(1, t+1):
    print('#%d'%ts, end =' ')
    n = int(input())
    pass_num = []
    for i in range(n):
        a, b = map(int, input().split())
        pass_num.append((a,b))

    P = int(input())
    for p in range(P):
        chk_num = int(input())
        cnt = 0
        for i in pass_num:
            if i[0] <= chk_num <= i[1]:
                cnt += 1
        print(cnt, end=' ')
    print('')