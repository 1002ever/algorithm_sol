from collections import deque

dx = [1, 10, 100, 1000]

def prime_chk():
    for i in range(2, 10000):
        j = i
        while 1:
            j += i
            if j >= 10000:
                break
            if prime_list[j] != j:
                continue
            prime_list[j] = 0

def bfs(start):
    global cnt
    q = deque()
    q.appendleft(start)
    visited.add(start)
    if start == target:
        return
    while q:
        cnt += 1
        for i in range(len(q)):
            cur = q.pop()
            for j in range(4):
                temp = cur
                temp = int(temp/dx[j])%10
                temp *= dx[j]
                temp = cur-temp
                for k in range(10):
                    if temp == target:
                        return
                    if temp not in visited and temp != cur and temp > 1000 and prime_list[temp] != 0:
                        q.appendleft(temp)
                        visited.add(temp)
                    temp += dx[j]
    return -1

prime_list = [0]*10000
for i in range(2, 10000):
    prime_list[i] = i
prime_chk()

t = int(input())
for tc in range(1, t+1):
    start, target = map(int, input().split())
    visited = set()
    cnt = 0
    if bfs(start) != -1:
        print(cnt)
    else:
        print('Impossible')
