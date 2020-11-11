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
        
<<<<<<< HEAD
    print(' '.join(answer))
    return ' '.join(answer)

solution('dsd sdasda  sdasd')
print('sd'.isalpha())
=======
    # print(answer)
    return ' '.join(answer)
>>>>>>> b047df88beb03f14db0f4469247c332b6c4ee792
