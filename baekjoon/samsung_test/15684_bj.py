# 삼성 역테 (백준 15684 - 사다리 조작)
# 무조건 다시 풀어보기.. pypy3으로 겨우 통과
# 시간 줄이는 방법 구상해보기

def ladder(frame):
    for i in range(n):
        cnt = 0
        cur = i
        while cnt < h:
            if cur < n-1 and frame[cnt][cur] == 1:
                cnt += 1
                cur += 1
                continue
            if cur > 0 and frame[cnt][cur-1] == 1:
                cnt += 1
                cur -= 1
                continue
            cnt += 1 
        if cur != i:
            return False
    return True

# 0 <= x < h , 0 <= y < n-1
def side_chk(x, y):
    if y-1 >= 0 and frame[x][y-1] == 1:
        return False
    if y+1 < n-1 and frame[x][y+1] == 1:
        return False
    return True

def dfs_bridge(x, y, z, cnt):
    global ans

    if cnt == z:
        if ladder(frame):
            ans = z
            return True
    else:
        if y >= n-1:
            y = 0
            x += 1
        for i in range(x, h):
            y = 0
            for j in range(y, n-1):
                if frame[i][j] == 1:
                    continue
                if side_chk(i, j):
                    frame[i][j] = 1
                    if dfs_bridge(i, j+2, z, cnt+1):
                        return
                    frame[i][j] = 0

n, m, h = map(int, input().split())
ans = -1
frame = [[0]*(n-1) for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    frame[a-1][b-1] = 1

for i in range(0, 4):
    dfs_bridge(0, 0, i, 0)
    if ans == i:
        break
print(ans)