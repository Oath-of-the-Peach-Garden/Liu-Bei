# JadenCase 문자열 만들기

# 공백이 여러 개인 경우
def solution(s):
    answer = []

    temp = s.split(' ')
    for word in temp:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append('')
    print(temp)
    return ' '.join(answer)
print(solution('3people  unFollowed me')+'/')