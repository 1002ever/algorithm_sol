t = int(input())

for ts in range(1, t+1):
    n = int(input())
    score_list = list(map(int, input().split()))
    sum_cnt = [False]*(sum(score_list)+1)
    sum_cnt[0] = True

    for i in range(len(score_list)):
        tmp = score_list[i]
        if sum_cnt[tmp] == False:
            print(tmp)
            sum_cnt[tmp] = True
        for j in range(len(score_list)):
            tmp += score_list[j]
            if sum_cnt[tmp] == False:
                print(tmp)
                sum_cnt[tmp] = True
    print(sum_cnt.count(True))