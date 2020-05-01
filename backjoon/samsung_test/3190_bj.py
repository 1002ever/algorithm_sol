# 백준 삼성 코테 기출 - 뱀(3190)

from collections import deque

# 상우하좌 순
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# snake 저장소
q = deque()

# head, tail 초기값
q.append([0,0])

def move_idx(cur_idx, dir):
    if dir == 'L':
        if cur_idx >= 1:
            cur_idx -= 1
        else:
            cur_idx = 3
    else:
        if cur_idx < 3:
            cur_idx += 1
        else:
            cur_idx = 0
    return cur_idx

def move(frame):
    head = q[-1]
    tail = q[0]
    m_x = head[0] + dx[midx]
    m_y = head[1] + dy[midx]
    head = [m_x, m_y]

    if 0 <= m_x < n and 0 <= m_y < n and frame[m_x][m_y] != 1:
        if frame[m_x][m_y] == 0:
            q.append([m_x, m_y])
            frame[m_x][m_y] = 1
            q.popleft()
            frame[tail[0]][tail[1]] = 0
            # 꼬리 짧아지면, tail 이동
        else:
            q.append([m_x, m_y])
            frame[m_x][m_y] = 1
        return 1
    else:
        return 0

n = int(input())
k = int(input())
frame = [[0]*n for _ in range(n)]
endchk = 1

ans = 0

# 사과 놓기
for i in range(k):
    x, y = map(int, input().split())
    frame[x-1][y-1] = 2

# 뱀 초기 위치
frame[0][0] = 1

# 초기 방향 우 => 초기 이동 인덱스 값 1
midx = 1

l = int(input())
chk_cnts = []
move_dir = []
for i in range(l):
    cnt, turn = input().split()
    chk_cnts.append(int(cnt))
    move_dir.append(turn)

while endchk:
    # 방향 바꾸는 때가 오면 바꿔주고 pop
    if len(chk_cnts) > 0 and chk_cnts[0] == ans:
        midx = move_idx(midx, move_dir[0])
        chk_cnts.pop(0)
        move_dir.pop(0)

    endchk = move(frame)
    ans += 1

print(ans)