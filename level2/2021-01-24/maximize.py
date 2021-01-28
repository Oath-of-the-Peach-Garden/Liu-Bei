# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257#

from collections import deque
from itertools import permutations
from copy import deepcopy


def solution(expression):
    answer = 0
    express_list = deque()
    num = ''
    for ex in expression:
        if ex not in ['+', '-', '*']:
            num += ex
        else:
            express_list.append(num)
            num = ''
            express_list.append(ex)
    else:
        express_list.append(num)

    orders = list(permutations(['+', '-', '*']))
    for order in orders:
        temp = deepcopy(express_list)
        temp.append(temp.popleft())
        for o in order:

            while temp[0] in ['*', '-', '+']:
                if temp[0] == o:
                    temp.popleft()
                    temp[-1] = eval(str(temp[-1])+o+str(temp.popleft()))
                else:
                    temp.append(temp.popleft())
                    temp.append(temp.popleft())
            else:
                temp.append(temp.popleft())
        if abs(temp[0]) > answer:
            answer = abs(temp[0])
    return answer
