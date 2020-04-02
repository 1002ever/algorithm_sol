def coms(a, b, c):
    if c == 0:
        return a+b
    elif c == 1:
        return a-b
    elif c == 2:
        return a*b
    else:
        if a < 0:
            tmp = (-a) // b
            return -tmp
        else:
            return a//b

def dfs(cnt, val):
    global maxn
    global minn
    if cnt == target_cnt:
        if maxn < val:
            maxn = val
        if minn > val:
            minn = val
    else:
        for i in range(len(com_cnt)):
            if com_cnt[i] > 0:
                com_cnt[i] -= 1
                dfs(cnt+1, coms(val, num_list[cnt+1], i))
                com_cnt[i] += 1

t = int(input())

for ts in range(1, t+1):
    maxn = -2147000000
    minn = 2147000000

    n = int(input())
    com_cnt = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    target_cnt = sum(com_cnt)

    dfs(0, num_list[0])
    print('#%d'%ts, maxn-minn)