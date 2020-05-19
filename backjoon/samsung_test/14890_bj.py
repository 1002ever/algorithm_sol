# 백준 삼성 코테 기출 ( 14890 - 경사로 )

def chk_road(road, ii):
    # print(ii, '번째')
    global ans
    idx = 0
    cur = road[idx]
    idx += 1
    cnt = 1
    
    while idx < n:
        # print(idx)
        if road[idx] == cur:
            # print('평지')
            cnt += 1
        elif road[idx]-cur == 1:
            # print('오르막길')
            if cnt < l:
                return
            else:
                cnt = 1
        elif cur-road[idx] == 1:
            # print('내리막길')
            chk = road[idx]
            if idx+l-1 >= n:
                return
            for i in range(1, l):
                if road[idx] != road[idx+i]:
                    return
            cnt = 0
            cur = road[idx+l-1]
            idx += l
            continue
        else:
            # print('진입 불가')
            return

        cur = road[idx]
        idx += 1
    ans += 1
    # print('채택')
            

n, l = map(int, input().split())
frame = [[] for _ in range(n)]
ans = 0

for i in range(n):
    frame[i] = list(map(int, input().split()))

for i in range(n):
    chk_road(frame[i], i)
frame = list(zip(*frame))
# print('행렬 전환')
for i in range(n):
    chk_road(frame[i], i)

print(ans)
