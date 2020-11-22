# 정수 내림차순으로 배치하기
def solution(n):
    return int(''.join(reversed(sorted(str(n)))))
