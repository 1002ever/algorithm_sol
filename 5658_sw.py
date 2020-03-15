t = int(input())

for ts in range(1, t+1):
    n, k = map(int, input().split())
    frame = input()
    num_list = []

    n_cnt = int(n/4)
    for j in range(n_cnt):
        frame = frame[-1] + frame[:len(frame)-1]
        for i in range(4):
            chk_num = frame[i * n_cnt:i * n_cnt + n_cnt]
            if chk_num not in num_list:
                num_list.append(frame[i*n_cnt:i*n_cnt+n_cnt])

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i], 16)
    num_list.sort(reverse=True)
    print('#%d'%ts, num_list[k-1])