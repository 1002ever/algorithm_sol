# 삼성 코테 기출 ( 백준 14891 - 톱니바퀴 )

# N극 = 0 / S극 = 1
def turn(idx, d):
    visited[idx] = 1

    if idx+1 < 4 and visited[idx+1] == 0:
        if frame[idx+1][6] != frame[idx][2]:
            turn(idx+1, d*(-1))
    if idx-1 >= 0 and visited[idx-1] == 0:
        if frame[idx-1][2] != frame[idx][6]:
            turn(idx-1, d*(-1))

    if d == 1:
        frame[idx] = [frame[idx][-1]] + frame[idx][:7]
    else:
        frame[idx] = frame[idx][1:] + [frame[idx][0]]

frame = [[] for _ in range(4)]
visited = []
ans = 0

for i in range(4):
    frame[i] = list(input())

k = int(input())
for i in range(k):
    visited = [0]*4
    idx, d = map(int, input().split())
    turn(idx-1, d)

for i in range(4):
    ans += (int(frame[i][0]) * 2 ** i)
print(ans)