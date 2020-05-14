def bin_chk(l, r, num, chk):
    if l > r:
        return 0
    m = (l+r)//2

    if a[m] > num:
        if chk == 0:
            return 0
        return bin_chk(l, m-1, num, 0)
    elif a[m] < num:
        if chk == 1:
            return 0
        return bin_chk(m+1, r, num, 1)
    else:
        return 1
        

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    ans = 0

    for num in b:
        if bin_chk(0, n-1, num, -1) == 1:
            ans += 1

    print('#%d'%tc, ans)
        