T = int(input())

for tc in range(1, T+1):
    print('#%d'%tc, end=' ')
    N, K = map(int, input().split())
    frame = [[] for _ in range(N)]
    cnt_sum = 0
    for n in range(N):
        frame[n] = list(map(int, input().split()))

    for i in range(N):
        cnt = 0
        word_cnt = 0
        for j in range(N):
            if frame[i][j] == 1:
                cnt += 1
            if cnt == K and frame[i][j] == 0:
                word_cnt += 1
                cnt = 0
                continue
            if cnt == K and j == N-1:
                word_cnt += 1
            if cnt > K or frame[i][j] == 0:
                cnt = 0
        cnt_sum += word_cnt
    
    for k in range(N):
        cnt = 0 
        word_cnt = 0
        for l in range(N):
            if frame[l][k] == 1:
                cnt += 1
            if cnt == K and frame[l][k] == 0:
                word_cnt += 1
                cnt = 0
                continue
            if cnt == K and l == N-1:
                word_cnt += 1
            if cnt > K or frame[l][k] == 0:
                cnt = 0
        cnt_sum += word_cnt

    print(cnt_sum)
            
    