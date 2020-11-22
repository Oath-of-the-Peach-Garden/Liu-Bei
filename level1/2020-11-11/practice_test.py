# 모의고사
def solution(answers):
    answer = []

    # 나머지 연산으로 반복
    # if answer == pattern1[idx%len(pattern1)]:
    # enumerate -> 반복문을 돌면서 인덱스도 같이 사용해야할 때 쓰면 된다. 값과 인덱스가 튜플형태로 리턴됨
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

def solution2(answers):
    answer = []

    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    scores = [0,0,0]
    for i,a in enumerate(answers):
        # print(f'i = {i}, a = {a}')
        if a == pattern1[i%len(pattern1)]:
            scores[0] += 1
        if a == pattern2[i%len(pattern2)]:
            scores[1] += 1
        if a == pattern3[i%len(pattern3)]:
            scores[2] += 1
    # print(f'scores = {scores}, max(scores) = {max(scores)}')
    answer = [std+1 for std, score in enumerate(scores) if max(scores) == score]

    return answer
        
print(solution([1,2,3,4,5,3,2,4,3,2,4,5,3,2,3,4,2,1,2,3]))
print(solution([1,2,3,4,5]))
print(solution2([1,2,3,4,5]))
