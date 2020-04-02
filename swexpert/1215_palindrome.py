T = 10
H = W = 8
frame = [[] for _ in range(H)]

# 회문 검사
def palindrome(word):
    leng = len(word)
    for c in range(int(leng/2)):
        if word[c] != word[-(c+1)]:
            return -1
    return 1

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    N = int(input())
    cnt = 0
    
    for i in range(8):
        frame[i] = input()
    
    # 가로 세로 N 길이 문자 뽑아서 회문 검사 후 cnt 증가
    for aa in range(H):
        for bb in range(H-N+1):
            word = frame[aa][bb:bb+N]
            if palindrome(word) == 1:
                cnt += 1
            word = ''
            for cc in range(N):
                word = word + frame[bb+cc][aa]
            if palindrome(word) == 1:
                cnt += 1
    print(cnt)

    
            