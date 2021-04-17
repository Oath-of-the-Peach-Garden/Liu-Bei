import heapq
import copy


def solution(operations):

    def redef(q):
        temp = copy.deepcopy(q)
        new_q = []
        while temp:
            t = heapq.heappop(temp)
            heapq.heappush(new_q, (-t[0], t[1]))

        return new_q

    answer = []
    min_q = []
    max_q = []
    for oper in operations:
        o, num = oper.split()
        num = int(num)
        if o == "I":
            heapq.heappush(min_q, (num, num))
            heapq.heappush(max_q, (-num, num))
        elif o == "D":
            if not min_q:
                continue

            if num == -1:
                heapq.heappop(min_q)
                max_q = redef(min_q)
            else:
                heapq.heappop(max_q)
                min_q = redef(max_q)
        # print(oper)
        # print(max_q)
        # print(min_q)
    # print(min_q, max_q)

    if min_q:
        _, min_value = heapq.heappop(min_q)
        _, max_value = heapq.heappop(max_q)

        answer = [max_value, min_value]
    else:
        answer = [0, 0]

    return answer


solution(["I 16", "D 1"])
solution(["I 7", "I 5", "I -5", "D -1"])
