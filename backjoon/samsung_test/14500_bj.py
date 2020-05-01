# 테트리미노 백준 삼성 코테 기출(14500)

# 상하좌우 순
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
frame = [[] for _ in range(n)]
ans = -2147000000
for i in range(n):
    frame[i] = list(map(int, input().split()))

cases = [
    # 작대기
    [1,1,1],
    [3,3,3],
    # 정사각형
    [1,3,0],
    # ㄱ자
    [1,1,3],
    [3,3,0],
    [0,0,2],
    [0,3,3],
    [1,1,2],
    [2,2,0],
    [0,0,3],
    [0,2,2],
    # 번개
    [1,3,1],
    [3,0,3],
    [1,2,1],
    [2,0,2],
    # ㅗ자
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3],
]

for i in range(n):
    for j in range(m):
        for k in range(15):
            x, y = i, j
            case_sum = frame[i][j]
            for l in range(len(cases[k])):
                x = x+dx[cases[k][l]]
                y = y+dy[cases[k][l]]
                if 0 > x or n <= x or 0 > y or m <= y:
                    break
                case_sum += frame[x][y]
                if l == len(cases[k])-1 and ans < case_sum:
                    ans = case_sum           
        for k in range(15, 19):
            x, y = i, j
            x1, y1 = x + dx[cases[k][0]], y + dy[cases[k][0]]
            if 0 > x1 or n <= x1 or 0 > y1 or m <= y1:
                continue
            x2, y2 = x + dx[cases[k][1]], y + dy[cases[k][1]]
            if 0 > x2 or n <= x2 or 0 > y2 or m <= y2:
                continue
            x3, y3 = x + dx[cases[k][2]], y + dy[cases[k][2]]
            if 0 > x3 or n <= x3 or 0 > y3 or m <= y3:
                continue
            case_sum = frame[x][y]+frame[x1][y1]+frame[x2][y2]+frame[x3][y3]
            if case_sum > ans:
                ans = case_sum

print(ans)