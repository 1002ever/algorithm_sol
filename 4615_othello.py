import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for ts in range(1, T+1):
    N, M = map(int, input().split())

    frame = [[0]*(N+1) for _ in range(N+1)]
    frame[int(N/2)][int(N/2)] = frame[int(N/2)+1][int(N/2)+1] = 2
    frame[int(N/2)+1][int(N/2)] = frame[int(N/2)][int(N/2)+1] = 1

    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    one_sum = 0
    two_sum = 0
    
    for i in range(M):
        x, y, c = map(int, input().split())
        frame[x][y] = c
        for j in range(8):
            m_x = x       # 돌 놓는 위치
            m_y = y
            cnt = 0
            while 1:
                m_x += dx[j]   # 8 방향 중 하나로 이동
                m_y += dy[j]
                # 프레임 밖으로 나가면 아웃
                if m_x == 0 or m_y == 0 or m_x == N+1 or m_y == N+1:
                    cnt = 0
                    break
                # 바로 같은 색 돌을 만나거나 0을 만나면 아웃
                if (frame[m_x][m_y] == c and cnt == 0) or frame[m_x][m_y] == 0:
                    cnt = 0
                    break
                # 다른 색도 만나고 왔으면서, 같은 색 돌을 만나면 아웃
                if frame[m_x][m_y] == c and cnt != 0:
                    break
                # 0이 아닌 다른 색을 만나면 cnt + 1
                if frame[m_x][m_y] != 0 and frame[m_x][m_y] != c:
                    cnt += 1
                

            for k in range(cnt):
                m_x -= dx[j]
                m_y -= dy[j]
                frame[m_x][m_y] = c

    for z in range(1, N+1):
        one_sum += frame[z].count(1)
        two_sum += frame[z].count(2)

    print('#%d'%ts, one_sum, two_sum)