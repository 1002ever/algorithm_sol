# swexpert - 10888 음식배달

from itertools import combinations

def cost_calc(store_list, home_list, frame):
    tmp = 0
    # 임대료
    for store in store_list:
        x, y = store
        tmp += frame[x][y]

    # 거리 가까운 곳 배달거리
    for home in home_list:
        min_dis = 2147000000
        x1, y1 = home
        for store in store_list:
            x2, y2 = store
            dis = abs(x1-x2) + abs(y1-y2)
            if dis < min_dis:
                min_dis = dis
        tmp += min_dis
    return tmp

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    frame = [[] for _ in range(n)]
    store_cand = []
    home_list = []
    ans = 2147000000
    for x in range(n):
        frame[x] = list(map(int, input().split()))
        for y in range(n):
            if frame[x][y] == 1:
                home_list.append([x, y])
            if frame[x][y] > 1:
                store_cand.append([x, y])

    store_len = len(store_cand)
    for i in range(1, store_len+1):
        store_list = list(combinations(store_cand, i))
        for j in range(len(store_list)):
            tmp = cost_calc(store_list[j], home_list, frame)
            if tmp < ans:
                ans = tmp
    print("#%d"%tc, ans)