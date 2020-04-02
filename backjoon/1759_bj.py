def dfs(idx, ans, cnt):
    if cnt == n:
        v_cnt = 0
        for i in range(len(vowel)):
            v_cnt += ans.count(vowel[i])

        if v_cnt >= 1 and len(ans) - v_cnt >= 2:
            for i in range(cnt):
                print(ans[i], end='')
            print('')
    else:
        if idx < len(alphas):
            tmp = ans + [alphas[idx]]
            dfs(idx+1, tmp, cnt+1)
            dfs(idx+1, ans, cnt)

n, tot_n = map(int, input().split())
alphas = input().split()
alphas.sort()
ans = []
vowel = ['a', 'e', 'i', 'o', 'u']

dfs(0, ans, 0)