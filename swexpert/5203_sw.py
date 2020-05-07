def chktriplet(cards, num):
    if cards[num] == 3:
        return 1
    else:
        return 0

def chkrun(cards, num):
    if num != 0 and num != 9:
        if cards[num-1] >= 1 and cards[num+1] >= 1:
            return 1
    if num <= 7:
        if cards[num+1] >= 1 and cards[num+2] >= 1:
            return 1
    if num >= 2:
        if cards[num-1] >= 1 and cards[num-2] >= 1:
            return 1
    return 0


t = int(input())

for tc in range(1, t+1):
    nums = list(map(int, input().split()))
    a = [0]*10
    b = [0]*10
    ans = 0

    for idx, num in enumerate(nums):
        chk = []
        chkab = 0
        if idx % 2 == 0:
            a[num] += 1
            chk.append(chktriplet(a, num))
            chk.append(chkrun(a, num))
            chkab = 1
        else:
            b[num] += 1
            chk.append(chktriplet(b, num))
            chk.append(chkrun(b, num))
            chkab = 2
        if sum(chk) >= 1:
            if chkab == 1:
                ans = 1
            else:
                ans = 2
            break

    print("#%d"%tc, ans)