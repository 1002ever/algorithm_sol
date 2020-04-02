T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    s, l = map(int, input().split())
    S = list(map(int, input().split()))
    L = list(map(int, input().split()))
    temp_sum = 0
    max_sum = -2147000000

    if len(S) > len(L):
        S, L = L, S

    for i in range(len(L)-len(S)+1):
        temp_sum = 0
        for j in range(len(S)):
            temp_sum += S[j]*L[i+j]
        if temp_sum > max_sum:
            max_sum = temp_sum
    
    print(max_sum)