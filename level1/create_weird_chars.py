# 이상한 문자 만들기
def solution(s):
    answer = []

    s = s.split(' ')
    for word in s:
        word = list(word)
        for ind in range(len(word)):
            word[ind] = word[ind].upper()
            if ind % 2: word[ind] = word[ind].lower()
        answer.append(''.join(word))
        
    # print(answer)
    return ' '.join(answer)