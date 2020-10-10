# # 백준 17779 게리맨더링2 - 삼성 코테 기출

# 테
dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

n = int(input())
frame = [[] for _ in range(n)]
part_frame = []

reg_cnt = [0]*5

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

                part_frame = [[0]*n for _ in range(n)]
                for dx in range(1, d1+1):
                    for dy in range(1, )