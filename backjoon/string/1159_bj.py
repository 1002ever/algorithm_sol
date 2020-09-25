# 백준 1159 - 농구 경기

n = int(input())
dict = {}
ans = set()

for i in range(n):
    name = input()
    try:
        dict[name[0]] += 1
        if dict[name[0]] >= 5:
            ans.add(name[0])
    except:
        dict[name[0]] = 1

ans = list(ans)
ans.sort()
if len(ans) == 0:
    print("PREDAJA")
else:
    print(''.join(ans))