def sep(p):
    if p[0] == ')':
        cnt = -1
    else:
        cnt = 1
    
    for i in range(1, len(p)):
        if p[i] == ')':
            cnt -= 1
        else:
            cnt += 1
        
        if cnt == 0:
            u, v = (p[:i+1], p[i+1:])
            break
    
    if right_chk(u):
        if v != '':
            v = sep(v)
        return u + v
    else:
        if v != '':
            v = sep(v)
        temp = ''
        for i in range(1, len(u)-1):
            if u[i] == '(':
                temp = temp + ')'
            else:
                temp = temp + '('
        return '(' + v + ')' + temp
        
        
def right_chk(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True
    

def solution(p):
    if p == '':
        return ''
    
    if right_chk(p):
        return p
    
    return sep(p)