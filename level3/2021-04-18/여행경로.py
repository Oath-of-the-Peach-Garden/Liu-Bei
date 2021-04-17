# 여행경로
from collections import defaultdict


def solution(tickets):
    answer = ["ICN"]

    cnt = len(tickets)

    paths = {}

    for ticket in tickets:
        if ticket[0] in paths:
            paths[ticket[0]].append(ticket[1])
            paths[ticket[0]].sort()
        else:
            paths[ticket[0]] = [ticket[1]]

    port = "ICN"

    # print(paths)
    while cnt:
        # print(cnt, port)
        port = paths[port].pop(0)
        answer.append(port)

        cnt -= 1

    return answer


# 2


def solution2(tickets):
    def dfs():
        temp = ["ICN"]
        answer = []

        while temp:
            port = temp[-1]

            if port not in routes or routes[port] == []:
                answer.append(temp.pop())
            else:
                temp.append(routes[port].pop(0))

        return answer[::-1]

    routes = defaultdict(list)
    for ticket in tickets:
        key, value = ticket
        routes[key].append(value)

    for key in routes:
        routes[key].sort()

    answer = dfs()
    # print(answer)

    return answer
