# 삼성 코테 기출 - 14888(연산자 끼워넣기)

def oper(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        return int(a/b)

def comb(op, cnt):
    global minimum
    global maximum

    if oper_cnt == cnt:
        res = nums[0]
        for i in range(n-1):
            res = oper(res, nums[i+1], op[i])
        if res < minimum:
            minimum = res
        if res > maximum:
            maximum = res
        return
    else:
        for i in range(4):
            if operators[i] > 0:
                op.append(i)
                operators[i] -= 1
                comb(op, cnt+1)
                op.pop()
                operators[i] += 1

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
minimum = 2147000000
maximum = -2147000000

# 연산자 수
oper_cnt = sum(operators)

comb([], 0)
print(maximum)
print(minimum)