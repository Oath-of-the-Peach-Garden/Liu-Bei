# 큰 수 만들기

def solution(number, k):
    answer = ''

    n = len(number)

    remove = [str(i) for i in range(n)]
    temp1 = remove[:]
    while 1:
        temp2 = []
        for i in temp1:
            for j in range(n):
                j = str(j)
                if j not in i:
                    temp2.append(str(i) + j)

        remove = temp2
        temp1 = temp2
        if len(remove[-1]) == k:
            break
    # print(remove)
    result = []
    for r in remove:
        temp_num = list(number)
        r = sorted(r, reverse=True)
        for ind in r:
            ind = int(ind)
            # print(
            # f'ind: {ind} temp_num {temp_num} temp_num[ind] {temp_num[ind]}')
            del temp_num[ind]
        result.append(int("".join(temp_num)))
        # print(f"result: {result}-----------------------")

    return max(result)


print(solution("1924", 2))
print(solution("1231234",	3))
print(solution("4177252841",	4))

# 큰 수 만들기


def solution1(number, k):
    # 숫자에서 문자를 다 지웠을 떄 나올 수 있는 각 자리의 최대값 비교?
    n = len(number)

    result_len = n - k

    temp = []
    for i, num in enumerate(number):
        if i <= k:
            n = num+"0"*(result_len-1)
            if n not in temp:
                temp.append(n)
            else:
                temp.append(n[:-1])
        else:
            temp.append(number[i:])
            break

    temp = list(map(int, list(reversed(sorted(temp)))))
    # print(temp)
    flag = [0] * result_len
    result = 0
    pre = ""
    for i in range(k):
        if len(pre) == len(str(temp[i])):

            result += int(str(temp[i])[1:])
        else:
            result += temp[i]
        if str(result)[-k+1:] == number[-k+1:]:
            break
        pre = str(temp[i])

    return result


print(solution1("1924", 2))
print(solution1("1231234",	3))
print(solution1("4177252841",	4))


# 큰 수 만들기

def solution3(number, k):
    # 숫자에서 문자를 다 지웠을 떄 나올 수 있는 각 자리의 최대값 비교?
    n = len(number)

    result_len = n - k

    temp = []
    for i, num in enumerate(number):
        if i <= k:
            n = num*result_len
            if n not in temp:
                temp.append(n)
            else:
                temp.append(n[:-1])
        else:
            temp.append(number[i]*len(number[i:]))
    temp = sorted(temp, key=lambda x: len(x), reverse=True)
    print(temp)

    pre_len = result_len
    result = [0]
    for t in temp:
        if pre_len == len(t):
            print(t, result[0])
            if result[result_len - pre_len] < int(t[0]):
                result[result_len - pre_len] = int(t[0])
                print(result[0])
        else:
            pre_len -= 1
            result.append(int(t[0]))
    print(result)


# 큰 수 만들기

def solution4(number, k):
    # 숫자에서 문자를 다 지웠을 떄 나올 수 있는 각 자리의 최대값 비교?
    n = len(number)
    number = list(number)
    result_len = n - k

    temp = []
    for i, num in enumerate(number):
        if i <= k:
            if [num, result_len] not in temp:
                temp.append([num, result_len])
            else:
                temp.append([num, result_len-1])
        else:
            temp.append([num, len(number[i:])])
    r = result_len
    result = ""
    # print(temp)
    while 1:
        r_temp = []
        for t in temp:
            if t[1] == r:
                r_temp.append(t)
        max_temp = max(r_temp)[0]

        for t in r_temp:
            if t[0] == max_temp and len(result) != r-1:
                result += max_temp
                ind = temp.index(t)
                del temp[:ind]
            else:
                t[1] -= 1
                if t[1] == 0:
                    ind = temp.index(t)
                    del temp[ind]
        r -= 1

        if r == 0:
            break

    return result


def solution5(number, k):
    answer = ""
    result_len = len(number) - k

    point = 0
    for i in range(result_len):
        max_num = "0"
        # for j in range(point+1, i+k+1):
        #     if max_num < number[j]:
        #         point = j
        #         max_num = number[j]
        temp_number = number[point:i+k+1]
        max_num = max(temp_number)
        point += temp_number.find(max_num) + 1
        # print(temp_number, max_num, point)
        answer += max_num

    return answer


def solution6(number, k):
    stack = []
    del_cnt = 0

    for i in range(len(number)):
        ind = len(stack) - 1

        while ind >= 0 and stack[ind] < int(number[i]) and del_cnt < k:
            del_cnt += 1
            stack.pop()
            ind = len(stack) - 1

        stack.append(int(number[i]))

    print(stack)
    if del_cnt < k:
        stack.pop()
    print(stack)

    return "".join(list(map(str, stack)))
