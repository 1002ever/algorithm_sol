from collections import deque

t=int(input())
for ts in range(1,t+1):
    n, m=map(int, input().split())
    nums_list = [[] for _ in range(m)]

    for i in range(m):
        nums_list[i] = list(map(int, input().split()))

    ans = deque()
    ans.extend(nums_list[0][:])

    t=1
    chk = False
    while t < m:
        for i in range(t*m):
            if ans[i] > nums_list[t][0]:
                chk = True
                idx = i
                break
        if chk:
            for i in range(n-1,-1,-1):
                ans.insert(idx, nums_list[t][i])
            t += 1
            chk=False
        else:   
            ans.extend(nums_list[t][:])
            t = t+1
    print('#%d'%ts, end=' ')
    for i in range(10):
        print(ans.pop(), end=' ')
    print('')
