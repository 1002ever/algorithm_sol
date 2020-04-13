t = int(input())

for ts in range(1, t+1):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))

    idx = 0
    for i in range(k):
        idx += m
        if idx > len(nums):
            idx = idx % len(nums)
        
        if idx == len(nums):
            insNum = nums[-1] + nums[0]
            nums.append(insNum)
        else:
            insNum = nums[idx-1] + nums[idx]
            nums.insert(idx, insNum)


    print("#%d"%ts, end=" ")
    cnt = 0
    for i in range(-1, -(len(nums)+1), -1):
        if cnt == 10:
            break
        print(nums[i], end=" ")
        cnt += 1
    print("")