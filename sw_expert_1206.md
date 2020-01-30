```python
import sys

sum = 0

sys.stdin = open("input.txt", "r")

for i in range(10):
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))

    idx = 2
    while 1:
        if max(heights[idx-2], heights[idx-1], heights[idx], heights[idx+1], heights[idx+2]) == heights[idx]:
            sum += heights[idx] - max(heights[idx-2], heights[idx-1], heights[idx+1], heights[idx+2])
            idx += 3
        else:
            idx += 1
        
        
        if idx > n-3:
            break
    print('#{} {}'.format(i+1, sum))
    sum = 0
```

