def ampersand(num):
    step = 1
    asum = 0
    ans = [0, 0]
    while asum + step < num:
        asum += step
        step += 1
    asum += step

    ans = [step, 1]
    while num != asum:
        asum -= 1
        ans[0] -= 1
        ans[1] += 1
    return ans

def sharp(nums):
    step = sum(nums)-1
    x, y = [1, step]
    ans = 0
    for i in range(1, step):
        ans += i
    
    while nums != [x, y]:
        ans += 1
        x += 1
        y -= 1
    ans+= 1
    return ans
    

T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    a, b = map(int,input().split())
    temp = []
    temp = ampersand(a)
    a, b = ampersand(b)
    temp[0] += a
    temp[1] += b
    
    print(sharp(temp))