# 삼성 A형 테스트 기출 - 16637 괄호 추가하기

ans = -2147000000

def calc(a, b, c):
    a = int(a)
    c = int(c)
    if b == '+':
        return a+c
    elif b == '-':
        return a-c
    else:
        return a*c

def calc_form(formula, calc_cand):
    global ans
    calc_cand.sort(reverse=True)
    # 괄호부터 계산
    for i in calc_cand:
        idx = calc_idx[i]
        tmp = calc(formula[idx-1], formula[idx], formula[idx+1])
        formula = formula[:idx-1] + str(tmp) + formula[idx+2:]
    while 1:
        a = ''
        b = ''
        c = ''
        chk = 0
        min_a = 0
        min_c = 0
        idx = 0
        for ch in range(len(formula)):
            if (formula[ch] == '+' or formula[ch] == '-' or formula[ch] == '*'):
                if chk == 1 and c != '':
                    idx = ch
                    break
                if chk == 1 and c == '':
                    min_c = 1
                    continue
                if a == '':
                    min_a = 1
                    continue
                chk = 1
                b = formula[ch]
                continue
            if chk == 0:
                a = a + formula[ch]
            else:
                c = c + formula[ch]

        if min_a == 1:
            a = '-' + a

        if min_c == 1:
            c = '-' + c

        if idx == 0:
            formula = calc(a, b, c)
            break
        else:
            formula = str(calc(a, b, c)) + formula[idx:]

    if ans < formula:
        ans = formula
        

def calc_comb(cnt, cnt2, calc_idx, calc_cand, rct_idx, formula):
    if cnt2 == cnt:
        calc_form(formula, calc_cand)
        return
    for i in range(rct_idx, len(calc_idx)):
        if i-1 in calc_cand:
            continue
        calc_cand.append(i)
        calc_comb(cnt+1, cnt2, calc_idx, calc_cand[:], i+2, formula)
        calc_cand.pop()

n = int(input())
calc_idx = list(range(1, n, 2))
formula = input()
calc_n = n // 2

if n == 1:
    ans = int(formula)
elif n == 3:
    ans = calc(formula[0], formula[1], formula[2])

for i in range(1, calc_n):
    calc_comb(0, i, calc_idx, [], 0, formula)

print(ans)