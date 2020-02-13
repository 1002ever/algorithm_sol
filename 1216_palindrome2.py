H = W = 100
frame = [[] for _ in range(H)]

# 회문 검사
def palindrome(word):
    leng = len(word)
    for c in range(int(leng/2)):
        if word[c] != word[-(c+1)]:
            return -1
    return 1

for ts in range(10):
    T = int(input())
    print('#%d'%T, end=' ')
    max_len = 1
    
    for i in range(H):
        frame[i] = input()
    
    for ll in range(2,(H+1)):
        for aa in range(H):
            for bb in range(H-ll+1):
                word = frame[aa][bb:bb+ll]
                if palindrome(word) == 1:
                    max_len = ll
                    break
                word = ''
                for cc in range(ll):
                    word = word + frame[bb+cc][aa]
                if palindrome(word) == 1:
                    max_len = ll
            if max_len == ll:
                break
    print(max_len)