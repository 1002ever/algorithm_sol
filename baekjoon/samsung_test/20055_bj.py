# 백준 20055 컨베이어 벨트 위의 로봇 - 삼성 코테 기출

from collections import deque

global zero_cnt

# 회전 시 올라가고 내려오는 위치 갱신
def turn_belt(up, down, n):
    if up == 0:
        x = 2*n-1
    else:
        x = up-1
    
    if down == 0:
        y = 2*n-1
    else:
        y = down-1
    
    return (x, y)

def move_robots(n, belt, robots, down_pos):
    leng = len(robots)
    
    # 현 로봇 위치 정보 돌면서
    # 한 칸씩 이동
    for i in range(leng-1, -1, -1):
        cur_pos = robots[i]
        if cur_pos == 2*n-1:
            next_pos = 0
        else:
            next_pos = cur_pos + 1
        
        # 내려가는 위치면 로봇 삭제
        if cur_pos == down_pos:
            robots.pop(i)
            continue
        
        # 아니라면 이동 가능한지 검사 후 이동
        if belt[next_pos] > 0 and (next_pos not in robots):
            robots[i] = next_pos
            belt[next_pos] -= 1
            if next_pos == down_pos:
                robots.pop(i)
        

n, k = map(int, input().split())

# 내구도 상태
belt = list(map(int, input().split()))
# 로봇 현 위치 리스트
robots = []

# 올라갈 박스 위치, 내려갈 박스 위치, 내구성 0인 칸 수 초기값
up_pos = 0
down_pos = n-1
zero_cnt = 0

fin_chk = False
stage = 0

while not fin_chk:
    # print('****', stage+1, '단계째****')

    # 1. 회전
    up_pos, down_pos = turn_belt(up_pos, down_pos, n)
    # print('###########')
    # print('회전 결과')
    # print(up_pos, down_pos)

    # 2. 로봇 이동(로봇이 있을 때만)
    if robots:
        move_robots(n, belt, robots, down_pos)
        # print('###########')
        # print('이동 했다면')
        # print(robots)

    # 3. 로봇 올리기
    if (up_pos not in robots) and belt[up_pos] > 0:
        robots.insert(0, up_pos)
        belt[up_pos] -= 1
        # print('###########')
        # print('올렸다면')
        # print(robots)

    stage += 1

    # print('###########')
    # print('결과', stage)
    # print(belt)
    # print(robots)

    if belt.count(0) >= k:
        print(stage)
        break

    