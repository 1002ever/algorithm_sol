```python
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
nums = list(range(1, 13))

for ts in range(1, T+1):
    n, k = list(map(int, input().split()))
    cnt = 0

    for i in range(1<<len(nums)):
        sub = []
        for j in range(len(nums)):
            if i & (1 << j):
                sub.append(nums[j])
        if k == sum(sub) and n == len(sub):
            cnt += 1
        
    print('#%d'%ts, cnt)





```

