t = int(input())

for tc in range(1, t+1):
    n = int(input())
    schedules = []
    times = []
    for i in range(n):
        schedule = tuple(map(int, input().split()))
        schedules.append(schedule)
    
    temp_min = 2147000000
    start_idx = -1
    for idx, item in enumerate(schedules):
        if temp_min > item[1]:
            temp_min = item[1]
            start_idx = idx
    times.append(schedules[start_idx])

    while 1:
        chk = 0
        temp_min = 2147000000
        for idx, item in enumerate(schedules):
            if times[-1][1] <= item[0] and temp_min > item[1]:
                chk = 1
                temp_min = item[1]
                next_idx = idx
        if chk == 1:
            times.append(schedules[next_idx])            
        else:
            break
    print("#%d"%tc, len(times))