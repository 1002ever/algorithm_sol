def solution(words, queries):
    
    result = []
    visited = []
    
    for i in range(len(queries)):
        query = queries[i]
        
        # 이미 방문한 것
        if queries.index(query) in visited:
            result.append(result[queries.index(query)])
            continue
            
        # 쿼리가 전부 ?일 때
        if query[0] == '?' and query[-1] == '?':
            cnt = 0
            for word in words:
                if len(word) == len(query):
                    cnt += 1
            visited.append(i)
            result.append(cnt)
            continue
        
        if query[0] == '?':
            start_idx = query.count('?')
            end_idx = len(query)
        else:
            start_idx = 0
            end_idx = query.index('?')
        
        cnt = 0
        for word in words:
            if len(word) != len(query):
                continue
            
            if word[start_idx:end_idx] == query[start_idx:end_idx]:
                cnt += 1
        result.append(cnt)
        visited.append(i)
        
    return result