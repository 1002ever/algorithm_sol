import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for ts in range(1, T+1):
    N, M = map(int, input().split())
    num = (N-(M-1))  
    paris = [[] for _ in range(N)]
    max_sum = -2147000000
    x, y = [0, 0]
    cnt = 0
    
    for i in range(N):
        paris[i] = list(map(int, input().split()))
    
    for j in range(num*num):
        temp_sum = 0
        sum_x = x
        sum_y = y
        for k in range(M*M):
            temp_sum += paris[sum_x][sum_y]
            sum_y+=1
            if k % M == M-1:
                sum_x +=1
                sum_y = y
        y += 1
        if y == num:
            x +=1
            y = 0
        if temp_sum > max_sum:
            max_sum = temp_sum

    print('#%d'%ts, max_sum)