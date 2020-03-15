def comb2(idx, cnt):
    global a_sum
    global b_sum
    if cnt == 2:
        a_sum += sij[a_list[idx[0]]][a_list[idx[1]]]
        a_sum += sij[a_list[idx[1]]][a_list[idx[0]]]
        b_sum += sij[b_list[idx[0]]][b_list[idx[1]]]
        b_sum += sij[b_list[idx[1]]][b_list[idx[0]]]
    else:
        for i in range(int(n/2)):
            if cnt > 0 and i < idx[-1]:
                continue
            if i not in idx:
                idx.append(i)
                comb2(idx, cnt+1)
                idx.pop()

def dfs(cnt):
    global a_list
    global b_list
    global a_sum
    global b_sum
    global minabs

    if cnt == int(n/2):
        a_sum = 0
        b_sum = 0
        comb2([], 0)
        absres = abs(a_sum-b_sum)
        if minabs > absres:
            minabs = absres
    else:
        for i in range(len(a_list)):
            temp = a_list.pop(i)
            if cnt > 0 and temp < b_list[-1]:
                a_list.insert(i,temp)
                continue
            b_list.append(temp)
            dfs(cnt+1)
            a_list.insert(i, temp)
            b_list.pop()

t = int(input())
a_sum = 0
b_sum = 0

for ts in range(1, t+1):
    n = int(input())
    minabs = 2147000000
    sij = [[] for _ in range(n)]
    a_list = list(range(n))
    b_list = []
    menu_visited = [1]*int(n/2)
    for i in range(n):
        sij[i] = list(map(int, input().split()))

    dfs(0)
    print('#%d'%ts, minabs)