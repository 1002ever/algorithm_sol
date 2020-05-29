t = int(input())

# 부모 & 조상 노드 list return
def find_pset(v, pset):
    if parents[v] == 0:
        return pset
    else:
        pset.append(parents[v])
        return find_pset(parents[v], pset)

# 해당 노드로부터 서브 tree 크기 파악
def cnt_sub(v):
    cnt = 0
    q = set()
    # 시작이 되는 서브트리 최상위
    q.add(v)
    cnt += 1

    while q:
        v = q.pop()
        for i in range(1, len(parents)):
            if parents[i] == v:
                q.add(i)
                cnt += 1
    return cnt

for tc in range(1, t+1):
    v, e, t1, t2 = map(int, input().split())
    e_infos = list(map(int, input().split()))
    parents = [0]*(v+1)
    common_p = 0

    ans = 0
    

    # 값이 바뀌지 않는, 즉 0이면 최상위 노드라는 의미
    for i in range(0, e*2, 2):
        parents[e_infos[i+1]] = e_infos[i]
    
    # 조상 리스트
    t1_pset = find_pset(t1, [])
    t2_pset = find_pset(t2, [])

    # 공통 조상 찾기
    for i in range(len(t1_pset)):
        if t1_pset[i] in t2_pset:
            common_p = t1_pset[i]
            break

    ans = cnt_sub(common_p)
    print('#%d'%tc, common_p, ans)
    

    