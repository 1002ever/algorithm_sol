```python
# [S/W 문제해결 기본] 2일차 - Sum

import sys
sys.stdin = open('input.txt', 'r')

for i in range(1, 11):
    sums = []
    ts = int(input())
    nums = [list(map(int, input().split())) for q in range(100)]
    trans_num = nums
    
    for j in range(100):            # 가로 합 추가
        sums.append(sum(nums[j]))

    l_sum = 0                       # 대각선 합 추가
    r_sum = 0
    for m in range(100):
        l_sum += nums[m][m]
        r_sum += nums[m][99-m]
    sums = sums + [l_sum, r_sum]
    
    for k in range(100):            # 세로 합 추가
        h_sum = 0
        for l in range(100):
            h_sum += nums[l][k]
        sums.append(h_sum)

    print('#%d'%ts, max(sums))
```

