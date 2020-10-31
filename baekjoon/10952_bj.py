# 그냥

def plus(a, b):
    return a+b
    
while 1:
    a, b = input().split()
    if [a, b] == ['0', '0']:
        break
    print(plus(int(a),int(b)))