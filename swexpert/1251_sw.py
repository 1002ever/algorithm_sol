t = int(input())

def prim():
    # 그래프 구성
    nodes = list()
    # 초기 노드
    nodes.append(islands.pop())
    dis_sum = 0

    # 현 그래프(nodes)에서 가장 가까운 정점 하나씩 추가
    while islands:
        min_dis = 0
        min_idx = -1
        tmp = -1
        for i in range(len(islands)):
            for j in range(len(nodes)):
                dis = (nodes[j][0] - islands[i][0])**2 + (nodes[j][1] - islands[i][1])**2
                # min_dis 초기값
                if i==0 and j==0:
                    min_dis = dis
                    min_idx = 0

                if dis < min_dis:
                    min_dis = dis
                    min_idx = i
                    tmp = j
        nodes.append(islands.pop(min_idx))
        dis_sum += min_dis

    return dis_sum


for tc in range(1, t+1):
    n = int(input())
    islands = []
    for i in range(2):
        islands.append(list(map(int, input().split())))
    islands = list(zip(*islands))
    e = float(input())

    ans = prim()
    ans = round(ans*e)
    print('#%d'%tc, ans)