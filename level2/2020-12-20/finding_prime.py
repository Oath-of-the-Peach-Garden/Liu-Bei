# 소수 찾기

def solution(numbers):
    answer = 0

    seqs = []
    temp = []

    n = [str(i) for i in range(len(numbers))]
    seqs += n
    temp += n
    while 1:
        nums = []
        for i in temp:
            for j in n:
                if j not in i:
                    nums.append(i+j)
        temp = nums
        seqs += nums
        if len(n) == len(nums[-1]):
            break

    temp = []
    for seq in seqs:
        num = ""
        for ind in seq:
            num += numbers[int(ind)]
        temp.append(num)

    temp = list(set(list(map(int, temp))))
    # print(temp)
    for t in temp:
        if t == 0 or t == 1:
            continue
        for i in range(2, t//2+1):
            if t % i == 0:
                break
        else:
            answer += 1

    return answer
