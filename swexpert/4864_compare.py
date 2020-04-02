T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    str1 = input()
    str2 = input()
    
    leng = len(str1)
    
    str_list = []
    for i in range(len(str2)-leng+1):
        str_list.append(str2[i:i+leng])
    
    if str1 in str_list:
        print(1)
    else:
        print(0)
                