# 스타수열
from collections import Counter


def solution(a):
    answer = -1
    elements = Counter(a)

    for k in elements.keys():
        if elements[k] <= answer:
            continue

        common = 0
        ind = 0
        # k = 3
        # [5,2,3,3,5,3]
        #
        while ind < len(a)-1:
            if (a[ind] != k and a[ind+1] != k) or (a[ind] == a[ind+1]):
                ind += 1
                continue
            common += 1
            ind += 2

        answer = max(common, answer)

    if answer == -1:
        return 0
    else:
        return answer * 2
