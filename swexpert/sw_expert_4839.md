```python
import sys
sys.stdin = open('sample_input.txt', 'r')

def bi_search(l, r, c):
    cnt = 0
    while 1:
        mid = int((l+r)/2)
        if mid == c:
            cnt += 1
            return cnt
        elif mid > c:
            r = mid
            cnt += 1
        else:
            l = mid
            cnt += 1 

T = int(input())
nums = list(range(1, 13))

for ts in range(1, T+1):
    p, a, b = list(map(int, input().split()))
    ans = ''

    a_cnt = bi_search(1, p, a)
    b_cnt = bi_search(1, p, b)
    
    if a_cnt > b_cnt:
        ans = 'B'
    elif a_cnt < b_cnt:
        ans = 'A'
    else:
        ans = 0
        
    print('#%d'%ts, ans)
```

