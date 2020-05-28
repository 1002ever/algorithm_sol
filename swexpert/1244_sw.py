# 구현 논리
# ( 바꾸는 기준 - 앞보다 뒤가 더 큰 경우 )
# 바꿀게 없음? = 이미 정렬 상태
#   1) 짝수 횟수 남았으면 그대로 return
#   2) 홀수 횟수 남았으면 ㄱ) 같은 card 있으면 
#                                       => 그것끼리 바꾸면 되므로 그대로 return
#                                  ㄴ) 같은 것이 없으면 맨 뒤에 두 개를 교환
#                                       => 가장 작은 두 숫자일 것이므로
 
# 바꿀게 있음?
#   1. 해당 단계의 방문max 보다 더 크면 바꾸고 횟수 증가
#   2. 각 단계 별 가장 큰 숫자를 방문 배열에 저장.
#                 ( 해당 단계에서 방문했던 가장 큰 숫자보다 더 작으면
#                   더 이상 탐색의 의미가 없어지므로 )

t = int(input())
chk = 0

def max_num(cnt):
    global ans
    global chk

    # 바꿀 것이 없음
    if max_cards == cards:
        if (m-cnt) % 2 == 0:
            ans = int("".join(cards))
            chk = 1
            return
        else:
            # 같은 요소가 없는 경우
            if len(cards) == len(set(cards)):
                cards[-1], cards[-2] = cards[-2], cards[-1]
            ans = int("".join(cards))
            chk = 1
            return

    # turn 수 다 다 채웠으면 int화하여 ans와 비교
    if cnt == m:
        temp = int("".join(cards))

        if temp > ans:
            ans = temp
        return

    else:
        for i in range(len(cards)):
            for j in range(i+1, len(cards)):
                if cards[i] < cards[j]:
                    cards[i], cards[j] = cards[j], cards[i]
                    if visited[cnt+1] < int("".join(cards)):
                        visited[cnt+1] = int("".join(cards))
                        max_num(cnt+1)
                        if chk == 1:
                            return
                    cards[i], cards[j] = cards[j], cards[i]
                    continue

for tc in range(1, t+1):
    chk = 0
    nums = input().split()
    cards = list(nums[0])
    m = int(nums[1])
    visited = [0]*(m+1)
    ans = -2147000000
    max_cards = sorted(cards, reverse=True)

    max_num(0)
    print('#%d'%tc, ans)