def battery(nums):
    global ans
    bat = 0
    for i in range(n):
        bat += frame[nums[i]-1][nums[i+1]-1]
        if bat > ans:
            return
    ans = bat

def perm(cnt, nums):
    # 경로 끝에는 1이 와야 함
    if cnt == n:
        nums.append(1)
        battery(nums)
        nums.pop()
        return
    for i in range(1, n+1):
        if visited[i] == 0:
            nums = nums + [i]
            visited[i] = 1
            perm(cnt+1, nums)
            nums.pop()
            visited[i] = 0
            
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    visited = [0]*(n+1)
    ans = 2147000000
    frame = [[] for _ in range(n)]
    for i in range(n):
        frame[i] = list(map(int, input().split()))
    # 무조건 경로는 1로 시작
    visited[1] = 1
    perm(1, [1])
    print("#%d"%tc, ans)