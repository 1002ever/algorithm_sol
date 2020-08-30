n = 5
build_frame = [
    [0,0,0,1],
    [2,0,0,1],
    [4,0,0,1],
    [0,1,1,1],
    [1,1,1,1],
    [2,1,1,1],
    [3,1,1,1],
    [2,0,0,0],
    [1,1,1,0],
    [2,2,0,1]
]

def solution(n, build_frame):
    frame = [[0]*n for _ in range(n)]
    
    ans = []
    
    for build in build_frame:
        print(ans)
        x, y, a, b = build
        # 설치 작업
        if b == 1:
            # 기둥
            if a == 0:
                # 바닥 위 기둥
                if y == 0:
                    frame[x][y] = 1
                    frame[x][y+1] = 1
                    ans.append([x,y,0])
                # 기둥 위 또는 보 끝 위의 기둥
                elif frame[x][y] == 1 or frame[x][y] == 2:
                    frame[x][y+1] = 1
                    ans.append([x,y,0])
            # 보
            else:
                print('보 추가', build)
                # 기둥이 왼쪽
                if frame[x][y] == 1:
                    frame[x][y] = 2
                    frame[x+1][y] = 2
                    ans.append([x,y,1])
                # 기둥이 오른쪽
                elif (frame[x][y] == 2 or frame[x][y] == 3) and frame[x+1][y] == 1:
                    frame[x][y] = 2
                    frame[x+1][y] = 2
                    ans.append([x,y,1])
                # 보 사이의 보
                elif frame[x][y] == 2 and frame[x+1][y] == 2:
                    frame[x][y] = 3
                    frame[x+1][y] = 3
                    ans.append([x,y,1])

            print('기둥이나 보 추가', ans)

        # 삭제 작업
        else:
            print(build)
            # 기둥
            if a == 0:
                if frame[x][y] == 1 and (frame[x][y+1] == 1 or frame[x][y+1] == 3):
                    frame[x][y] = 0
                    if frame[x][y+1] == 1:
                        frame[x][y+1] = 0
                    ans.pop(ans.index([x,y,0]))
            else:
                if frame[x][y] == 2 and frame[x+1][y] == 2:
                    frame[x][y] = 0
                    frame[x+1][y] = 0
                    ans.pop(ans.index([x,y,1]))
    
    ans = sorted(ans, key = lambda x : (x[0], x[1], x[2]))   
    
    return ans

print(solution(n, build_frame))