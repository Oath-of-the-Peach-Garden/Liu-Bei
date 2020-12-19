# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):  # [3, 0, 6, 1, 5]
    n = len(citations)
    citations.sort(reverse=True)    # [6, 5, 3, 1, 0]
    i = 0
    while citations[i] > i:         # 6 > 0 - 5 > 1 - 3 > 2
        i += 1                      # i ++ -> i=3
        if i == n:                  # 1 > 3에서 탈출 -> 이 때 i(3)이 정답
            break                   # if문의 조건문을 while문에 넣으면 citations의 길이보다 하나 더 돌게 돼서 런타임에러가 나오는 듯

    return i


# 인용횟수를 내림차순으로 정렬
# while문을 돌리면서 i가 citations[i]보다 작거나 i가 citations의 길이만큼 커졌을 경우 탈출
# 인용 횟수 citations[i]이하인 논문이 citations[i]개(i) 있을 때
