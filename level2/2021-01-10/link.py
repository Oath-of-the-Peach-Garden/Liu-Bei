# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):

    pre = words[0][0]   # 앞단어의 끝자리를 기억
    number = 0  # 번호  1,2,3,1,2,3
    order = 0   # 차례  1,1,1,2,2,2,
    for i, word in enumerate(words):
        number = i % n
        order = i // n
        if pre != word[0] or word in words[:i]:  # 단어가 직전과 이어지지 않거나, 한번 나온 단어일 경우 끝남
            break
        else:
            pre = word[-1]  # 규칙에 맞는 단어를 말했을 경우 끝글자를 저장
    else:
        number = -1         # 끝까지 탈락자가 생기지 않음
        order = -1

    return [number+1, order+1]
