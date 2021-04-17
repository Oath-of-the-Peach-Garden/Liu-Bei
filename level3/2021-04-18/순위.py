# 순위
def solution(n, results):
    answer = 0

    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for result in results:
            a, b = result
            if a == i:
                wins[i].add(b)
            if b == i:
                loses[i].add(a)

        for win in loses[i]:
            wins[win].update(wins[i])

        for lose in wins[i]:
            loses[lose].update(loses[i])

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1

    return answer
