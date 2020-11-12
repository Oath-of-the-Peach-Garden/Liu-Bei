# k번째 수
# i-1부터 j까지 자르기
# k-1 수 append

# 다른 사람 코드
# list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)) -> 해석 필요
# i,j,k = command -> 코드 가독성이 높아질듯
# def solution(array, commands): return [sorted(array[i-1:j])[k-1] for i,j,k in commands] -> list comprehension를 사용해서 파이썬스러움


def solution(array, commands):
    answer = []

    for command in commands:
        temp = array[:]
        num = sorted(temp[command[0]-1:command[1]])
        # print(num)
        # print(num[command[2]-1])
        answer.append(num[command[2]-1])


    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))