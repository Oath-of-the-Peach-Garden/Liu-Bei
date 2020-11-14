# 모의고사
def solution(answers):
    answer = []

    # 나머지 연산으로 반복
    # if answer == pattern1[idx%len(pattern1)]:
    # enumerate -> 이게 뭐지
    std_answer = [
        [1,2,3,4,5]*(int(len(answers)/5)+1),
        [2,1,2,3,2,4,2,5]*(int(len(answers)/8)+1),
        [3,3,1,1,2,2,4,4,5,5]*(int(len(answers)/10)+1)
    ]

    # print(std_answer)
    score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == std_answer[0][i]:
            score[0] += 1
        if answers[i] == std_answer[1][i]:
            score[1] += 1
        if answers[i] == std_answer[2][i]:
            score[2] += 1
        

    return [std for std in [1,2,3] if max(score) == score[std-1]]
print(solution([1,2,3,4,5,3,2,4,3,2,4,5,3,2,3,4,2,1,2,3]))
print(solution([1,2,3,4,5]))
