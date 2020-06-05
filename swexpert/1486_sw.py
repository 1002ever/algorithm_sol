from collections import deque

t = int(input())

def bfs():
    global ans

    q = deque()
    # 큐에 현 top 높이와 idx 저장
    # 일단 한 명만 썼을 때를 q에 저장
    for i in range(len(heights)):
        q.appendleft((heights[i], i))
        if heights[i] > b:
            ans = abs(heights[i]-b)

    # 순차적으로 더해나가며 큐에 적재(조합)
    while q:
        h, idx = q.pop()
        idx += 1
        while idx < len(heights):
            if h+heights[idx] >= b:
                if abs(h + heights[idx] - b) < ans:
                    ans = abs(h + heights[idx] - b)
            else:
                q.appendleft((h+heights[idx], idx))

            idx += 1

for tc in range(1, t+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()
    ans = 2147000000
    
    bfs()

    print('#%d'%tc, ans)