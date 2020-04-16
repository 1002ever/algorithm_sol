def node_sum(l):
    # 리프 노드이면 리턴
    if nums[l] != -1:
        return nums[l]
    # 리프 노드가 아니면, 자식 노드를 합한 결과를 리턴
    else:
        # 자식이 2개 있을 때
        if l*2+1 <= n:
            return node_sum(l*2) + node_sum(l*2+1)
        # 자식이 1개만 있을 때
        else:
            return node_sum(l*2)

t = int(input())

for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    ans = 0
    # 리프 노드가 아니라면 -1 값을 저장
    nums = [-1]*(n+1)
    # 리프 노드에 입력 값을 저장
    for i in range(m):
        a, b = map(int, input().split())
        nums[a] = b

    ans = node_sum(l)
    print('#%d'%tc, ans)