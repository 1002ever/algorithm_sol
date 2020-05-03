# 백준 삼성 코테 기출 (14501 - 퇴사)

def dfs(idx, income):
    global ans

    if idx >= n:
        if ans < income:
            ans = income
        return

    # idx 부터 재귀 진입
    for i in range(idx, n):
        # 다음 가능한 일이 있으면 재귀
        if i+schedules[i][0]-1 < n:
            idx = i+schedules[i][0]
            dfs(idx, income+schedules[i][1])
        # 해당 인덱스 일이 불가능 하면 재귀 탈출
        else:
            if ans < income:
                ans = income
            continue
        
n = int(input())

schedules = []
ans = -2147000000

for i in range(n):
    schedule = tuple(map(int, input().split()))
    schedules.append(schedule)

dfs(0, 0)
print(ans)