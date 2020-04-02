import sys
sys.stdin = open('sample_input.txt', 'r')

def palindrome(word):
    leng = int(len(word)/2)
    for i in range(leng):
        if word[i] != word[-(i+1)]:
            return -1
    return 1

T = int(input())

for ts in range(1, T+1):
    N, M = map(int, input().split())
    frame = [[] for _ in range(N)]
    print('#%d'%ts, end=' ')
    ans=0
    for n in range(N):
        frame[n] = input()

    for i in range(N):
        for j in range(N-M+1):
            word = frame[i][j:j+M]
            if palindrome(word) == 1:
                print(word)
                ans = 1
                break
            word = ''
            for k in range(M):
                word = word + frame[j+k][i]
            if palindrome(word) == 1:
                print(word)
                ans = 1
                break
        if ans == 1:
            break