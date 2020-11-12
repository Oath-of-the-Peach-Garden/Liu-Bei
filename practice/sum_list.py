# 행렬의 덧셈
def solution(arr1, arr2):
    answer = [[]]

    for ind1 in range(len(arr1)):
        if len(answer)-1 < ind1: answer.append([])
        for ind2 in range(len(arr1[ind1])):
            answer[ind1].append(arr1[ind1][ind2] + arr2[ind1][ind2])

    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(list(zip([1,2],[2,3])))