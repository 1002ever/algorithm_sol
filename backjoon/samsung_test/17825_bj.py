# 백준 17825 주사위 윷놀이 - 삼성 코테 기출

ans = -2147000000

def dfs(sums, cnt, frame, horse_state, nums):
    global ans
    if cnt == 10:
        if sums > ans:
            ans = sums
        return

    for i in range(4):
        bef = horse_state[i]
        if horse_state[i] != -1:
            if horse_state[i] == 0 or horse_state[i] == 10 or horse_state[i] == 20 or horse_state[i] == 30 or horse_state[i] == 25 or horse_state[i] == 40:
                cur = horse_state[i]
                if len(frame[cur])-1 < nums[cnt]:
                    next = -1
                else:
                    next = frame[cur][nums[cnt]]
            else:
                cur_route = horse_state[i][0]
                cur_idx = frame[cur_route].index(horse_state[i])
                next_idx = cur_idx+nums[cnt]
                if next_idx >= len(frame[cur_route]):
                    next = -1
                else:
                    next = frame[cur_route][next_idx]

            if next == -1:
                horse_state[i] = -1
                dfs(sums, cnt+1, frame, horse_state, nums)
                horse_state[i] = bef
            else:
                if next not in horse_state:
                    horse_state[i] = next
                    if next == 10 or next == 20 or next == 30 or next == 40 or next == 25:
                        dfs(sums+next, cnt+1, frame, horse_state, nums)
                    else:
                        dfs(sums+next[1], cnt+1, frame, horse_state, nums)
                    horse_state[i] = bef

# 시작점 0, 도착점 -1
# 교차점 10, 20, 30
# 중앙지점 25
frame = {
    0: [0, [0, 2], [0, 4], [0, 6], [0, 8], 10, [0, 12], [0, 14], [0, 16], [0, 18], 20, [0, 22], [0, 24], [0, 26], [0, 28], 30, [0, 32], [0, 34], [0, 36], [0, 38], 40, -1],
    10: [10, [10, 13], [10, 16], [10, 19], 25, [25, 30], [25, 35], 40, -1],
    20: [20, [20, 22], [20, 24], 25, [25, 30], [25, 35], 40, -1],
    25: [25, [25, 30], [25, 35], 40, -1],
    30: [30, [30, 28], [30, 27], [30, 26], 25, [25, 30], [25, 35], 40, -1],
    40: [40, -1]
}

horse_state = [0]*4
nums = list(map(int, input().split()))

dfs(0, 0, frame, horse_state, nums)

print(ans)