t = int(input())

def rsp(a, b):
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2) or (a == b):
        return 1
    else:
        return -1

def game(cards):
    if len(cards) == 2:
        if rsp(cards[0][1], cards[1][1])==1:
            return cards[0]
        else:
            return cards[1]

    elif len(cards) == 3:
        if rsp(cards[0][1], cards[1][1])==1:
            if rsp(cards[0][1], cards[2][1])==1:
                return cards[0]
            else:
                return cards[2]
        else:
            if rsp(cards[1][1], cards[2][1])==1:
                return cards[1]
            else:
                return cards[2]
    else:
        be = (1 + len(cards)) // 2
        bef = cards[:be]
        aft = cards[be:]
        b = game(bef)
        a = game(aft)
        if rsp(b[1], a[1]) == 1:
            return b
        else:
            return a


for ts in range(1, t+1):
    n = int(input())
    temp = list(map(int, input().split()))
    idx = range(1, len(temp)+1)
    cards = list(zip(idx, temp))

    ans = game(cards)
    print('#%d'%ts, ans[0])