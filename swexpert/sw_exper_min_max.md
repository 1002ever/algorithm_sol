```python
import sys

sys.stdin = open("sample_input.txt", "r")

a = int(input())

for i in range(a):
    num = int(input())
    nums = list(map(int, input().split(' ')))
    print('#{} {}'.format(i+1, max(nums)-min(nums)))
```

