# 삼성 코테 기출 - (백준 5373 - 큐빙)

t = int(input())

def side_idx_sel(face_idx):
    idx_12 = []
    # 위아래
    if face_idx == 0 or face_idx == 1:
        faces = (idx_dict['F'], idx_dict['R'], idx_dict['B'], idx_dict['L'])
        if face_idx == 0:
            for i in range(12):
                idx_12.append((faces[i//3], 0, i%3))
        else:
            for i in range(12):
                idx_12.append((faces[i//3], 2, i%3))
    # 앞뒤
    elif face_idx == 2 or face_idx == 3:
        faces = (idx_dict['U'], idx_dict['R'], idx_dict['D'], idx_dict['L'])
        if face_idx == 2:
            for i in range(3):
                idx_12.append((faces[0], 2, i))
            for i in range(3):
                idx_12.append((faces[1], i, 0))
            for i in range(3):
                idx_12.append((faces[2], 0, 2-i))
            for i in range(3):
                idx_12.append((faces[3], 2-i, 2))
        else:
            for i in range(3):
                idx_12.append((faces[0], 0, i))
            for i in range(3):
                idx_12.append((faces[1], i, 2))
            for i in range(3):
                idx_12.append((faces[2], 2, 2-i))
            for i in range(3):
                idx_12.append((faces[3], 2-i, 0))
    # 좌우
    else:
        faces = (idx_dict['U'], idx_dict['F'], idx_dict['D'], idx_dict['B'])
        if face_idx == 4:
            for i in range(9):
                idx_12.append((faces[i//3], i%3, 0))
            for i in range(3):
                idx_12.append((faces[3], 2-i, 2))
        else:
            for i in range(9):
                idx_12.append((faces[i//3], i%3, 2))
            for i in range(3):
                idx_12.append((faces[3], 2-i, 0))
    return idx_12
            
            

def face_turn(face_idx, dir):
    temp = [[0]*3 for _ in range(3)]
    if dir == '-':
        for i in range(3):
            for j in range(3):
                temp[i][j] = frame[face_idx][j][2-i]
    else:
        for i in range(3):
            for j in range(3):
                temp[i][j] = frame[face_idx][2-j][i]
    frame[face_idx] = temp

for tc in range(1, t+1):
    n = int(input())
    orders = input().split()
    # frame = [
    #     # 위-아래-앞-뒤-왼-오른 순
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    # ]
    frame = [
        # 위-아래-앞-뒤-왼-오른 순
        [['w']*3 for _ in range(3)],
        [['y']*3 for _ in range(3)],
        [['r']*3 for _ in range(3)],
        [['o']*3 for _ in range(3)],
        [['g']*3 for _ in range(3)],
        [['b']*3 for _ in range(3)],
    ]
    idx_dict = {
        'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5,
    }
    
    for order in orders:
        # 해당 면 회전
        face_turn(idx_dict[order[0]], order[1])
        # 해당 면 옆 영향받을 인덱스 선정
        side_idx = side_idx_sel(idx_dict[order[0]])
        # 옆면 방향 판단하여 회전
        temp = [0] * 12
        if order == 'U-' or order == 'D+' or order == 'L+' or order == 'R-' or order == 'F+' or order == 'B-':
            for i in range(3):
                temp[i] = frame[side_idx[i+9][0]][side_idx[i+9][1]][side_idx[i+9][2]]
            for i in range(9):
                temp[i+3] = frame[side_idx[i][0]][side_idx[i][1]][side_idx[i][2]]
        else:
            for i in range(9):
                temp[i] = frame[side_idx[i+3][0]][side_idx[i+3][1]][side_idx[i+3][2]]
            for i in range(3):
                temp[i+9] = frame[side_idx[i][0]][side_idx[i][1]][side_idx[i][2]]
        for i in range(12):
            frame[side_idx[i][0]][side_idx[i][1]][side_idx[i][2]] = temp[i]

    for i in range(3):
        print(''.join(frame[0][i]))