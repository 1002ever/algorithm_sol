# 백준 8958 - OX퀴즈

n = int(input())
scores = []
for i in range(n):
    scores.append(input())

for score in scores:
    ans = 0
    cur_score = 0
    for char in score:
        if char == 'O':
            cur_score += 1
            ans += cur_score
        else:
            cur_score = 0
    print(ans)