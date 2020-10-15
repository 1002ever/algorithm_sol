# 백준 삼성 코테 기출 ( 스타트와 링크 - 14889)
# 다시 풀어봐야겠는데..? 코드가 너무 더럽,

tempsum = 0
suma = 0
sumb = 0

def team_sum(idx, cnt, team):
    global tempsum

    if idx >= int(n/2):
        return
    if cnt == 2:
        duo = []
        for i in range(n):
            if visited2[i] == 1:
                duo.append(i)
        tempsum += frame[duo[0]][duo[1]]
        tempsum += frame[duo[1]][duo[0]]
        return 
    else:
        for i in range(idx, int(n/2)):
            if visited2[team[i]] == 0:
                visited2[team[i]] = 1
                team_sum(i, cnt+1, team)
                visited2[team[i]] = 0

def comb(idx, cnt):
    global suma
    global sumb
    global tempsum
    global ans

    if idx >= n:
        return
    if cnt == int(n/2):
        start = []
        link = []
        
        for i in range(n):
            if visited[i] == 0:
                start.append(i)
            else:
                link.append(i)
        
        tempsum = 0
        team_sum(0, 0, start)
        suma = tempsum
        tempsum = 0
        team_sum(0, 0, link)
        sumb = tempsum

        diff = abs(suma - sumb)
        if ans > diff:
            ans = diff
        return
    else:
        for i in range(idx, n):
            if visited[i] == 0:
                visited[i] = 1
                comb(i, cnt+1)
                visited[i] = 0

n = int(input())

frame = [[] for _ in range(n)]
visited = [0]*n
visited2 = [0]*n
ans = 2147000000

for i in range(n):
    frame[i] = list(map(int, input().split()))

comb(0, 0)
print(ans)