# 구명보트

# 1
def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    temp = []
    for i in range(n-1, 0, -1):
        if i in temp:
            continue
        for j in range(i):
            if j in temp or people[i] + people[j] > limit:
                continue
            # print(people[i] + people[j])
            elif people[i] + people[j] <= limit:
                # print([i,j])
                # temp += [i, j]
                temp += [i, j]
                answer += 1
                break
        # print("------------")
    answer = n - answer
    # print(temp)

    return answer


# 2
def solution(people, limit):
    answer = 0
    people.sort()
    sp = 0
    ep = len(people) - 1

    while sp < ep:
        if people[sp] + people[ep] > limit:
            answer -= 1
            ep -= 1
        else:
            sp += 1
        answer += 1

    return answer
