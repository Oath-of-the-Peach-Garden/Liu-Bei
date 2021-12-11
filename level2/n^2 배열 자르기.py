# 프로그래머스 level2 n^2 배열 자르기
# https://programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    # n = 4
    # left = 7
    # right = 14
    answer = []
    # 각각 n으로 나눈 몫으로 찾아야할 행이 몇번째 행인지 계산
    for i in range(left//n, right//n+1):
      # n이 4일 때
      # 0: 1, 2, 3, 4 -> 1 한 개 + 1+1 ~ n
      # 1: 2, 2, 3, 4 -> 2 두 개 + 2+1 ~ n
      # 2: 3, 3, 3, 4 -> 3 세 개 + 3+1 ~ n
      # 3: 4, 4, 4, 4 -> 4 네 개
      # => (i+1이 i+1개 + i+2 ~ n) 규칙에 따라 수를 넣어줌
        answer += [i+1] * (i+1) + list(range(i+2, n+1))
    # answer에서 left의 위치는 n으로 나눈 나머지
    # 0            1            2            3
    # 1, 2, 3, 4 / 2, 2, 3, 4 / 3, 3, 3, 4 / 4, 4, 4, 4
    #                       7                     14
    #              0  1  2  3
    start = left % n  # 3
    # 끝 값은 right - left로 계산
    return answer[start:start+(right-left+1)]
