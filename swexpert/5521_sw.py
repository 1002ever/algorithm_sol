t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    friends = [set() for _ in range(n+1)]
    # 상원이의 직접 친구
    bests = set()
    # 상원이의 친구의 친구
    bests2 = set()
    ans = 0
    # 관계를 돌며, 각자의 친구 관계 정리
    for i in range(m):
        a, b = map(int, input().split())
        friends[a].add(b)
        friends[b].add(a)
        # 상원이의 친구는 따로 기록
        if 1 in (a, b):
            if a == 1:
                bests.add(b)
            else:
                bests.add(a)
    bests = list(bests)
    # 상원이의 친구들의 친구들을 조사
    for best in bests:
        # 상원이의 친구들의 친구들을 set으로 모음
        bests2.update(list(friends[best]))
    # 상원이의 친구들을 set으로 모음
    bests2.update(bests)
    # 친구가 있는 상황이면 본인을 뺌
    ans = len(bests2)
    if ans > 0:
        ans -= 1

    print('#%d'%tc, ans)