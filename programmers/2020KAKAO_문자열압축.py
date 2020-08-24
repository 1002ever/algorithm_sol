def rep_chk(s, cur_idx, step):
    chk_str = s[cur_idx:cur_idx+step]
    next_idx = cur_idx + step
    cnt = 1
    
    while next_idx+step-1 < len(s):
        if chk_str == s[next_idx:next_idx+step]:
            cnt += 1
            next_idx += step
            continue
        else:
            # 뒤가 다르고 0이면 -1
            if cnt == 1:
                return -1
            # 뒤가 다르고 여태 같은게 있었다면 cnt return
            else:
                return cnt
    if cnt == 1:
        return -1
    else:
        return cnt
            

def solution(s):
    s_leng = len(s)
    min_leng = 2147000000
    
    if len(s) == 1:
        return 1
    
    # 문자열 묶는 단위(step) > 1 ~ 절반 길이
    for step in range(1, (s_leng//2)+1):
        cur_idx = 0
        temp_s = ''
        while (cur_idx+step-1 < s_leng):
            res = rep_chk(s, cur_idx, step)
            if res == -1:
                temp_s = temp_s + s[cur_idx:cur_idx+step]
                cur_idx += step
            else:
                temp_s = temp_s + str(res) + s[cur_idx:cur_idx+step]
                cur_idx += (res*step)
                
        if cur_idx < s_leng:
            temp_s = temp_s + s[cur_idx:]
                
        if len(temp_s) < min_leng:
            min_leng = len(temp_s)
    
        
    return min_leng