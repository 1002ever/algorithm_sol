def dfs(day, income):
    global max_in
    if day <= n and day+table[day][0] <= n+1:
        for i in range(day+table[day][0], n+2):
            dfs(i, income+table[day][1])
    else:
        if income > max_in:
            max_in = income

max_in = -2147000000
n = int(input())
table = [[0]]
for i in range(n):
    table.append(list(map(int, input().split())))

for i in range(1, n+1):
    dfs(i, 0)
print(max_in)