# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1

    clothes_dict = {}

    for clothe in clothes:
        if clothe[1] in clothes_dict:
            clothes_dict[clothe[1]] += 1
        else:
            clothes_dict[clothe[1]] = 1
        print(clothes_dict)

    for key in clothes_dict:
        print(clothes_dict[key])
        answer *= clothes_dict[key]

    return answer


print(solution([['yellow_hat', 'headgear'], [
      'blue_sunglasses', 'eyewear'], ['green_turban', "headgear"]]))
