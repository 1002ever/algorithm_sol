import sys
sys.stdin = open('input.txt', 'r')

for T in range(10):
    ts = int(input())
    frame = [[] for _ in range(100)]
    testX = []
    ansX = -1
    lastM = 'd'
    minimum = 2147000000
    for i in range(100):
        frame[i] = list(map(int, input().split()))
        if i == 0:
            for j in range(100):
                if frame[0][j] == 1:
                    testX.append(j)

    for x in testX:
        cnt = 0   # 이동 수
        col = x   # 초기 시작점
        des = 0   
        while des != 99:
            if (lastM == 'l' or lastM == 'r'):
                des += 1
                cnt += 1
                lastM = 'd'
                continue
            if col > 0 and frame[des][col-1] == 1:
                col -= 1
                cnt += 1
                while frame[des+1][col] != 1:
                    col -= 1
                    cnt += 1
                lastM = 'l'
                continue
            if col < 99 and frame[des][col+1] == 1:
                col += 1
                cnt += 1
                while frame[des+1][col] != 1:
                    col += 1
                    cnt += 1
                lastM = 'r'
                continue
            else:
                des += 1
                cnt += 1
                lastM = 'd'
        if minimum > cnt:
            minimum = cnt
            ansX = x

    print('#%d'%ts, ansX)