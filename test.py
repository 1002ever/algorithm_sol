def solution(info, query):
    dict_info = {
        'cpp': {
            'backend': { 
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            }
        },
        'java': {
            'backend': { 
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            }
        },
        'python': {
            'backend': { 
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            }
        }
    }
    
    for inf in info:
        inf = inf.split(" ")
        dict_info[inf[0]][inf[1]][inf[2]][inf[3]].append(int(inf[4]))
        
    for que in query:
        que = que.split("and")
        print(que)
        
    print(dict_info)

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)