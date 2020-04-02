T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    str1 = list(input())
    leng1 = len(str1)
    str2 = list(input())
    leng2 = len(str2)

    maxc = -2147000000
    
    for i in range(leng1):
        if maxc < str2.count(str1[i]):
            maxc = str2.count(str1[i])
    print(maxc)
    