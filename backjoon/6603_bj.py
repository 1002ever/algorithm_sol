def dfs(nums, cnt):
    if cnt == 6:
        for i in range(6):
            print(nums[i], end=' ')
        print('')

    for i in range(1, k[0]+1):
        if len(nums) == 0 and i > k[0] - 5:
            return
        if visited[i] == False:
            if len(nums) == 0 and i <= k[0]-5:
                temp = nums[:] + [k[i]]
                visited[i] = True
                dfs(temp, cnt + 1)
                visited[i] = False
                continue
            elif nums[-1] < k[i]:
                temp = nums[:] + [k[i]]
                visited[i] = True
                dfs(temp, cnt + 1)
                visited[i] = False
                continue

while 1:
    k = list(map(int, input().split()))
    visited = [False]*(k[0]+1)
    if k == [0]:
        break
    dfs([], 0)
    print('')