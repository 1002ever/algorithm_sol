# 13458 시험감독

n = int(input())
subjects = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

# 우선 총감독 무조건 각 반에 투입
for i in range(n):
    subjects[i] -= b
    if subjects[i] < 0:
        subjects[i] = 0
    ans += 1

for i in range(n):
    # 부감독으로 나눈 몫 만큼 더하되, 나머지 남으면 +1
    ans += (subjects[i] // c)
    if subjects[i] % c > 0:
        ans += 1

print(ans)