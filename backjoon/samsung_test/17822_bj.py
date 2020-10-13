# 백준 17822 원판 돌리기 - 삼성 코테 기출

n, m, t = map(int, input().split())
nums = [[] for _ in range(n+1)]

for i in range(1, n+1):
    nums[i] = list(map(int, input().split()))

def turn(numbers, cnt, dir):
    if dir == 0:
        tmp_nums = numbers[len(numbers)-cnt:] + numbers[:len(numbers)-cnt]
    else:
        tmp_nums = numbers[cnt:] + numbers[:cnt]
    return tmp_nums

def del_same(nums, n, m):
    del_idx = []

    for i in range(1, n+1):
        for j in range(m):
            if nums[i][j] == 0:
                continue
            
            # 원판 내 검사
            be = j-1
            af = j+1
            # 맨 끝인 경우 인덱스 변환
            if j == 0:
                be = m-1
            if j == m-1:
                af = 0
            if nums[i][be] == nums[i][j]:
                del_idx.append((i, be))
                del_idx.append((i, j))
            if nums[i][af] == nums[i][j]:
                del_idx.append((i, af))
                del_idx.append((i, j))

            # 다른 원판 검사
            if i < n:
                if nums[i][j] == nums[i+1][j]:
                    del_idx.append((i, j))
                    del_idx.append((i+1, j))
            if i > 1:
                if nums[i][j] == nums[i-1][j]:
                    del_idx.append((i, j))
                    del_idx.append((i-1, j))
    
    del_idx = list(set(del_idx))

    for idx in del_idx:
        x, y = idx
        nums[x][y] = 0

    if len(del_idx) == 0:
        res = 0
    else:
        res = 1

    return (nums, res)

for z in range(t):
    x, d, k = map(int, input().split())
    # m번 회전하면 제자리이므로
    k = k % m
    # 1번 규칙, x 배수 원판 회전
    cnt = 1
    tmp_x = x
    while tmp_x <= n:
        if tmp_x > n:
            break
        nums[tmp_x] = turn(nums[tmp_x], k, d)
        cnt += 1
        tmp_x = x*cnt

    # 2번 규칙
    chk = 0
    # 인접 중복 수 체크 및 제거
    nums, chk = del_same(nums, n, m)

    # 2-2 같은 수 없는 경우
    if chk == 0:
        total = 0
        n_cnt = n*m
        for i in range(1, n+1):
            total += sum(nums[i])
            n_cnt -= nums[i].count(0)
        if total > 0:
            n_avg = total / n_cnt
        else:
            n_avg = 0

        for i in range(1, n+1):
            for j in range(m):
                if nums[i][j] == 0:
                    continue
            
                if nums[i][j] < n_avg:
                    nums[i][j] += 1
                elif nums[i][j] > n_avg:
                    nums[i][j] -= 1

ans = 0
for i in range(1, n+1):
    ans += sum(nums[i])


print(ans)