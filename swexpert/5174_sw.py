from collections import deque

t = int(input())

for tc in range(1, t+1):
    e, n = map(int, input().split())
    nums = list(map(int, input().split()))
    # 인접리스트 1번 부터 읽으려고 e+2까지 해줌
    adj_list = [[] for _ in range(e+2)]
    visited = [0]*(e+2)
    
    # cnt는 방문점 수
    cnt = 1
    q = deque()
    for i in range(0, len(nums), 2):
        adj_list[nums[i]].append(nums[i+1])
    
    q.append(n)
    while q:
        v = q.pop()
        for i in range(len(adj_list[v])):
            if visited[adj_list[v][i]] == False:
                cnt += 1
                q.append(adj_list[v][i])
    print('#%d'%tc, cnt)