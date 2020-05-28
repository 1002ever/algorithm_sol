def dfs(cnt, dis):
    global ans
 
    if cnt == n:
        dis += abs(end[0] - cur[0]) + abs(end[1] - cur[1])
        if ans > dis:
            ans = dis
    else:
        for i in range(n):
            if visited[i] == 0:
                # 방문처리, 현위치 변경
                visited[i] = 1
                dis += (abs(cur[0] - cus_xy[i*2]) + abs(cur[1] - cus_xy[i*2+1]))
                temp = [cur[0], cur[1]]
                cur[0], cur[1] = cus_xy[i*2], cus_xy[i*2+1]
 
                # 현재 이동 거리가 최소여야 dfs 진입
                if dis < ans:
                    dfs(cnt+1, dis)
 
                # 방문해제, 현위치 초기화
                visited[i] = 0
                dis -= (abs(temp[0] - cus_xy[i*2]) + abs(temp[1] - cus_xy[i*2+1]))
                cur[0], cur[1] = temp[0], temp[1]
                 
 
t = int(input())
 
for tc in range(1, t+1):
    n = int(input())
    # 0번 회사 / 1번 집 / 2번 ~ 고객집
    xys = list(map(int, input().split()))
    # 배달원 현 위치
    cur = [xys[0], xys[1]]
    # 최종 목적지
    end = [xys[2], xys[3]]
    # 고객 좌표
    cus_xy = xys[4:]
    visited = [0]*(n)
 
    ans = 2147000000
    dfs(0, 0)
    print('#%d'%tc, ans)