t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    # team을 각각 set으로 관리
    teams = [i for i in range(n+1)]
    ans = 0

    papers = list(map(int, input().split()))

    for i in range(0, m*2, 2):
        # 1. 팀번호 작은거 저장
        team_num = min(teams[papers[i]], teams[papers[i+1]])
        # 2. 팀번호 컸던거에 작은거를 저장 = 팀 통합
        # 기존에 컸던 팀 번호를 temp에 저장
        temp = teams[max(teams[papers[i]], teams[papers[i+1]])]
        teams[max(teams[papers[i]], teams[papers[i+1]])] = team_num

        for i in range(1, n+1):
            if teams[i] == temp:
                teams[i] = team_num

    ans = len(set(teams[1:]))
    print('#%d'%tc, ans)