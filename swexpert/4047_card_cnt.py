import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    print('#%d'%i, end=' ') 
    temp = input()
    cards = []
    cnt = [13] * 4
    error = 0
    alpha_idx = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
    n = int(len(temp) / 3)

    for j in range(0, 3*n, 3):
        cards.append([temp[j:j+3]])
        cnt[alpha_idx[temp[j]]] -= 1
    
    for k in range(n-1):
        for l in range(k+1, n):
            if cards[k] == cards[l]:
                error = 1
    
    if error == 1:
        print('ERROR')
    else:
        for m in range(4):
            print(cnt[m], end=' ')
        print('')
