# 백준 16235 나무 재테크 - 삼성 코테 기출

def spring_summer():

    dead_trees = []

    # 봄
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] <= nuts[i][j]:
                    nuts[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    dead_trees.append((i, j, trees[i][j][k]//2))

    for i in range(len(dead_trees)):
        trees[dead_trees[i][0]][dead_trees[i][1]].pop()
    
    # 여름
    while dead_trees:
        x, y, z = dead_trees.pop()
        nuts[x][y] += z
    
def fall():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for d in range(8):
                        mx = i+dx[d]
                        my = j+dy[d]
                        if 0 > mx or mx >= n or 0 > my or my >= n:
                            continue
                        trees[mx][my].insert(0, 1)

def winter():
    for i in range(n):
        for j in range(n):
            nuts[i][j] += a[i][j]

def year():
    spring_summer()
    fall()
    winter()

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())

a = [[0]*n for _ in range(n)]
nuts = [[5]*n for _ in range(n)]
# 나무는 3차원
trees = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        trees[i][j] = []

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for i in range(k):
    year()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans) 