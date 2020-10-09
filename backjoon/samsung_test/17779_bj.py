# # 백준 17779 게리맨더링2 - 삼성 코테 기출

# n = int(input())
# frame = [[] for _ in range(n)]
# part_frame = [[0]*n for _ in range(n)]

# reg_cnt = [0]*5

# for i in range(n):
#     frame[i] = list(map(int, input().split()))

# for x in range(n-2):
#     for y in range(1, n-1):
#         for d1 in range(1, y):
#             for d2 in range(1, n-y+1):
#                 # range 초과 확인
#                 if x+d1 >= n or y-d1 < 0:
#                     continue
#                 if x+d2 >= n or y+d2 >= n:
#                     continue
#                 if x+d1+d2 >= n or y-d1+d2 >= n:
#                     continue