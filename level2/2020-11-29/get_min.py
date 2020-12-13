# 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    # 제일 작은 수와 제일 큰 수를 곱한 값의 합이 최소값임
    for a, b in zip(A, B):
        answer += a*b

    return answer


print(solution([1, 4, 2], [5, 4, 4]))
