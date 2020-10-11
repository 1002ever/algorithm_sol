# 백준 17779 게리맨더링2 - 삼성 코테 기출

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

n = int(input())
frame = [[] for _ in range(n)]
part_frame = []

reg_cnt = [0]*5
ans = 2147000000

for i in range(n):
    frame[i] = list(map(int, input().split()))

for x in range(n-2):
    for y in range(1, n-1):
        for d1 in range(1, n):
            if x+d1 >= n or y-d1 < 0:
                break
            for d2 in range(1, n-y+1):
                if y-d1+d2 < 0 or y-d1+d2 >= n or x+d1+d2 >= n or y+d2 >= n or x+d2 >= n:
                    break

                imp = 0
                part_frame = [[0]*n for _ in range(n)]
                mx, my = x, y
                for i in range(4):
                    if i % 2 == 0:
                        dir = d1
                    else:
                        dir = d2
                    for j in range(dir):
                        mx = mx + dx[i]
                        my = my + dy[i]
                        if mx < 0 or mx >= n or my < 0 or my >= n:
                            imp = 1
                            break
                        part_frame[mx][my] = 5
                    if imp == 1:
                        break
                if imp == 1:
                    continue
                for i in range(n):
                    if part_frame[i].count(5) == 2:
                        for j in range(part_frame[i].index(5)+1, n):
                            if part_frame[i][j] == 0:
                                part_frame[i][j] = 5
                            else:
                                break
                
                for i in range(n):
                    for j in range(n):
                        if part_frame[i][j] != 5:
                            if i < x+d1 and j <= y:
                                part_frame[i][j] = 1
                            elif i <= x+d2 and y < j < n:
                                part_frame[i][j] = 2
                            elif x+d1 <= i < n and j < y-d1+d2:
                                part_frame[i][j] = 3
                            else:
                                part_frame[i][j] = 4
                
                reg_cnt = [0]*5
                for i in range(n):
                    for j in range(n):
                        cur = part_frame[i][j] - 1
                        reg_cnt[cur] += frame[i][j]
                if max(reg_cnt) - min(reg_cnt) < ans:
                    ans = max(reg_cnt) - min(reg_cnt)

print(ans)