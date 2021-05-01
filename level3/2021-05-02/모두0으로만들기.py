# 모두 0으로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/76503
from collections import defaultdict


answer = 0


def solution(a, edges):

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    def dfs(u, v):
        global answer
        for node in graph[u]:
            if node != v:
                dfs(node, u)
        answer += abs(a[u])
        a[v] += a[u]
        a[u] = 0
    dfs(0, 0)

    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
