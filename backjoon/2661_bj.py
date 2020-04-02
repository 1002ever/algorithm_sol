n = int(input())
nums = [1,2,3]
ans = [1]

# i 번째 자리 추가
for i in range(2, n+1):
    print(i)
    for num in nums:
        ans.append(num)
        err = 0
        # 1자리 수열부터 반 길이 수열까지 검사
        for j in range(1, i//2 + 1):
            be = ans[len(ans)-2-(2*(j-1)):len(ans)-j]
            af = ans[len(ans)-j:]
            print(be, af)
            if be == af:
                err = 1
                break
        if err == 1:
            ans.pop()
        else:
            break
    tmp = list(map(str, ans))
    print(''.join(tmp))