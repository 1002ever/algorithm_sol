from itertools import combinations

# 궁수가 공격할 적 선택 후 그를 list로 return
def select_enemy(enemies, archers, x, d):

    enemy_idx_set = set()

    # 궁수 순회
    for archer in archers:

        # 지금까지 가장 가까운 적 최소 거리
        dist = 2147000000
        # 지금까지 가장 가까운 적 인덱스
        enemy_idx = -1

        #  적 순회하며 dist, enemy_idx 갱신
        for idx, enemy in enumerate(enemies):
            tmp_dist = abs(enemy[0] - x) +  abs(enemy[1] - archer)
            # 사정거리 안쪽이면 고려해보기
            if d >= tmp_dist:
                # 지금까지 가장 가까운 거리이면 갱신
                if dist > tmp_dist:
                    dist = tmp_dist
                    enemy_idx = idx
                # 거리가 같다면 y 비교가 필요
                if dist == tmp_dist:
                    # 현재 y가 더 작다면 갱신
                    if enemies[idx][1] < enemies[enemy_idx][1]:
                        enemy_idx = idx
        
        if enemy_idx != -1:
            enemy_idx_set.add(enemy_idx)

    enemy_idx_list = list(enemy_idx_set)
    enemy_idx_list.sort(reverse=True) 
    return enemy_idx_list



n, m, d = map(int, input().split())
frame = [[] for _ in range(n)]
enemies = []

for i in range(n):
    frame[i] = list(map(int, input().split()))
    for j in range(m):
        if frame[i][j] == 1:
            enemies.append([i, j])

archers = combinations(range(m), 3)

# 궁수 경우의 수를 모두 순회
for archer_case in archers:

    tmp_enemies = [[] for _ in range(len(enemies))]
    for i in range(len(enemies)):
        tmp_enemies[i] = enemies[i][:]

    # 해당 케이스에 대해서 제거할 적이 없을 때까지
    while tmp_enemies:
        # 1. 제거 대상 선정
        enemy_list = select_enemy(tmp_enemies, archer_case, n, d)

        # 2. 제거
        for idx in enemy_list:
            tmp_enemies.pop(idx)

        # 3. 이동