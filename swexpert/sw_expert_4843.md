```python
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for ts in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = []
    
    print('#%d'%ts, end =' ')
    for i in range(10):
        if i % 2:
            nums = sorted(nums, reverse=True)
            ans.append(nums.pop())
        else:
            nums = sorted(nums)
            ans.append(nums.pop())
        print(ans[i], end=' ')
    print('')

```

