words = input()
bomb = input()

chk_stk = []

# 폭탄이 존재한다면
if bomb in words:
    # 글자 하나씩 추가
    for idx, word in enumerate(words):
        chk_stk.append(word)

        if len(chk_stk) >= len(bomb):
            chk = 1
            for i in range(len(bomb)):
                if bomb[-(i+1)] != chk_stk[-(i+1)]:
                    chk = 0
                    break
            if chk == 1:
                for i in range(len(bomb)):
                    chk_stk.pop()

    res = ''.join(chk_stk)
else:
    res = words

if len(res) > 0:
    print(res)
else:
    print('FRULA')