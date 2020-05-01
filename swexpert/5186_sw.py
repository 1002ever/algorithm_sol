t = int(input())

for tc in range(1, t+1):
    ans = ''
    n = float(input())
    cnt = 1
    while n != 0:
        if cnt > 12:
            ans = 'overflow'
            break
        if n >= 2**(-cnt):
            ans = ans + '1'
            n -= 2**(-cnt)
        else:
            ans = ans + '0'
        cnt += 1

    print("#%d"%tc, ans)