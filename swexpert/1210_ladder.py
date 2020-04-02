for ts in range(10):
    T = int(input())
    print('#%d' % T, end=' ')
    frame = [[] for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]

    # 출발점 인덱스 저장
    one_idx = []
    for i in range(100):
        frame[i] = list(map(int, input().split()))
        if i == 0:
            for j in range(100):
                if frame[i][j] == 1:
                    one_idx.append(j)

    # 2 발견 시 시작점 index 출력 후 빠져나감
    # 미 발견 시 visited 초기화 후 다시 탐색
    for c in one_idx:
        cc = c
        visited[0][cc] = 1
        r = 0
        while r < 99:
            if cc + 1 < 100 and frame[r][cc + 1] == 1 and visited[r][cc + 1] == False:
                cc += 1
            elif cc - 1 >= 0 and frame[r][cc - 1] == 1 and visited[r][cc - 1] == False:
                cc -= 1
            elif r < 99:
                r += 1
            visited[r][cc] = True

        if frame[99][cc] == 2:
            print(c)
            break
        visited = [[0] * 100 for _ in range(100)]