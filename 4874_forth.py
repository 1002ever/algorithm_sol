t = int(input())

for ts in range(1, t + 1):
    print('#%d' % ts, end=' ')
    cal = input().split()
    num = []
    ans = 0

    for c in cal:
        if c == '.':
            break
        if c == '+' or c == '-' or c == '*' or c == '/':
            try:
                b = num.pop()
                a = num.pop()
                if c == '+':
                    num.append(a + b)
                elif c == '-':
                    num.append(a - b)
                elif c == '*':
                    num.append(a * b)
                else:
                    num.append(a / b)
            except:
                ans = -1
        else:
            num.append(int(c))

    if ans == -1 or len(num) != 1:
        print('error')
    if ans == 0 and len(num) == 1:
        num[0] = int(num[0])
        print(num[0])