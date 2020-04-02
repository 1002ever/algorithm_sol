def pows(res, idx):
    global ans
    if idx == n:
        if sum(res) >= b and ans > sum(res):
            ans = sum(res)
    else:
        res.append(h_list[idx])
        tmp = res[:]
        pows(tmp, idx+1)
        res.pop()
        pows(res, idx+1)

t = int(input())

for ts in range(1, t+1):
    n, b = map(int, input().split())
    h_list = list(map(int, input().split()))
    ans = 2147000000

    pows([], 0)
    print('#%d'%ts, ans-b)