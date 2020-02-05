import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    print('#%d'%i)
    before = [0, 1, 0]
    N = int(input())
    for j in range(1, N+1):
        if j==1:
            print(1)
            continue        
        cur=[]
        for k in range(j):
            cur.append(before[k]+before[k+1])
        for l in range(len(cur)):
            print(cur[l], end=' ')
        print('')
        cur.insert(0,0)
        cur.append(0)
        before = cur