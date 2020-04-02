ans = 0
n, m = map(int, input().split())
nums = list(map(int, input().split()))
if len(nums) >= 2:
    true_p = set(nums[1:])
else:
    true_p = set()
false_p = set()

parties = [[] for _ in range(m)]
for i in range(m):
    temp = list(map(int, input().split()))
    if len(temp) > 1:
        parties[i] = set(temp[1:])

for i in range(m):
    for j in range(m):
        if len(true_p.intersection(parties[j])) >= 1:
            true_p.update(parties[j])

for i in range(m):
    if len(true_p.intersection(parties[i])) == 0:
        ans += 1
print(ans)