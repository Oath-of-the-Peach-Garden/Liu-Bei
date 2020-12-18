# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    num_list = \
        sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    # map: 모두 str형으로 바꿔줌
    # x*3:
    # 2,20가 있을 때 이어붙였을 때 최대로 나올 수 있는 수는 220이지만 내림차순으로 정렬하면 202가 결과값으로 나옴,
    # 이 경우에 문자열 곱하기를 사용해서 222, 202020으로 만든 후 내림차순으로 정렬하면 문자열은 인덱스 0부터 비교하여 정렬되기 떄문에
    # 220을 만들 수 있다. 3을 곱한 이유는 문제에서 원소의 최대값이 1000이라고 제한을 주었기 때문

    # 문자열로 값을 반환하면 0000이 결과인 경우가 있기 때문에 이 경우 0을 반환해주기 위해 int로 변환하여 0으로 만든 후 str로 다시 변환해준다.
    return str(int("".join(num_list)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([450, 453, 456]))


def solution2(numbers):
    answer = ''
    num_list = sorted(list(map(str, numbers)),
                      key=lambda x: x[0], reverse=True)
    print(num_list)

    pn = 0
    while len(num_list) != pn:
        temp = []

        pre = num_list[pn][0]
        # print(pn, num_list[pn][0])
        while len(num_list) > pn and pre == num_list[pn][0]:
            temp.append(num_list[pn])
            pn += 1
        temp = sorted(temp, key=lambda x: max(x))
        print(temp)
        answer += \
            "".join(temp)
    return "".join(num_list)


print(2, solution2([6, 10, 2]))
print(2, solution2([3, 30, 34, 5, 9]))
print(2, solution2([450, 453, 456]))
