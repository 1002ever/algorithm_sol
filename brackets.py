T = int(input())

for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    test_brackets = input()
    stack_bracket = []
    ans = 1
    for i in test_brackets:
        if i == '(' or i == '{':
            stack_bracket.append(i)
        elif i == ')':
            if len(stack_bracket)>0 and stack_bracket[-1]=='(':
                    stack_bracket.pop()
            else:
                ans = -1
                break
        elif i == '}':
            if len(stack_bracket)>0 and stack_bracket[-1]=='{':
                    stack_bracket.pop()
            else:
                ans = -1
                break

    if len(stack_bracket) == 0 and ans == 1:
        print(1)
    else:
        print(0)