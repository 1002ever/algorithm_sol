from operator import itemgetter

t = int(input())

def findP(x):
    if group[x] == x:
        return x
    else:
        return findP(group[x])

for tc in range(1, t+1):
    v, e = map(int, input().split())
    group = list(range(v+1))
    e_list = []
    ans = 0
    for i in range(e):
        e_list.append(list(map(int, input().split())))
    e_list.sort(key=itemgetter(2))
    
    idx = 0
    while len(set(group)) != 1:
        a = findP(e_list[idx][0])
        b = findP(e_list[idx][1])
        if a == b:
            idx += 1
            continue
        head = min(a, b)
        sub = max(a, b)
        if head == a:
            group[e_list[idx][1]] = head
        else:
            group[e_list[idx][0]] = head

        for g in range(0,v+1):
            if group[g] == sub:
                group[g] = head
        
        ans += e_list[idx][2]

    print('#%d'%tc, ans)