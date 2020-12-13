# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = []

    temp = []

    for ar1 in arr1:
        cnt = 0
        ind2 = 0
        while cnt < len(arr2[0]):
            ind1 = 0
            sum = 0
            print(f'cnt {cnt} ----------------------------------------------')
            for ar2 in arr2:
                sum += ar1[ind1] * ar2[ind2]
                print(
                    f' ar1[{ind1}] {ar1[ind1]} ar2[{ind2}] {ar2[ind2]} -> {ar1[ind1] * ar2[ind2]} += {sum}')
                ind1 += 1
            ind2 += 1
            temp.append(sum)
            print('------------------------------------------')
            cnt += 1

        print(temp)
        answer.append(temp)
        temp = []

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
               [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))


# 다른 사람 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
