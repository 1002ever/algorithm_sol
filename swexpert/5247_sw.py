# 5247
from collections import deque

# 4가지 연산
def comp(num, i):
    if i == 0:
        return num+1
    elif i == 1:
        return num-1
    elif i == 2:
        return num*2
    else:
        return num-10

def find(n, m):
    q = deque()
    # 이미 체킹한 숫자면 재탐색 안하도록 방문 set
    visited = set()
    
    visited.add(n)
    q.append(n)
    cnt = 0

    # 연산 깊이(횟수)는 cnt로 판단
    while q:
        cnt += 1
        for i in range(len(q)):
            n = q.pop()
            for i in range(4):
                num = comp(n, i)
                if num == m:
                    return cnt
                if 0 < num < 1000000 and num not in visited:
                    visited.add(num)
                    q.appendleft(num)

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    ans = find(n, m)

    print('#%d'%tc, ans)