```python
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    reds = []
    blues = []
    cnt = 0
    n = int(input())
    for j in range(n):
        temp = []
        info = list(map(int, input().split()))
        for k in range(info[0], info[2]+1):
            for l in range(info[1], info[3]+1):
                temp.append((k, l))
        if info[4] == 1:
            reds = reds + temp
        else:
            blues = blues + temp
            
    for red in reds:
        if red in blues:
            cnt += 1
    print('#%d'%i, cnt)
        
```

