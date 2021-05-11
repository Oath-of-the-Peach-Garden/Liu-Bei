# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter


def solution(N, stages):
    answer = []

    user_cnt = len(stages)

    user_stages = Counter(stages)

    print(user_stages)
    failures = []
    for stage in range(1, N+2):
        failure = user_stages[stage]/user_cnt if user_cnt else 0
        failures.append((-failure, stage))
        user_cnt -= user_stages[stage]

    failures.sort()
    print(failures)
    for fail in failures:
        answer.append(fail[1])
    return answer


print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))

# collections 모듈의 Counter 클래스를 사용해서 스테이지에 머물고 있는 사람 수를 dict 형태로 만듦
# 1부터 N까지의 스테이지의 실패율을 계산하여 failures 리스트에 -를 붙여(역정렬했을 때 작은 스테이지가 앞에 나오지 않아서 -으로 정렬) 스테이지와 함께 넣어주고 실패율을 기준으로 정렬
# 정렬된 리스트에서 스테이지 번호만 answer에 넣어줌
