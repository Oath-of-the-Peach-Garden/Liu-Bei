# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    global temp, answer
    answer = len(words)+1
    words = [begin] + words

    check = [0] * len(words)

    def word_chk(word1, word2):
        cnt = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                cnt += 1

        return cnt == 1
    temp = 0

    def bfs(n):
        global temp, answer
        if words[n] == target:

            if temp < answer:
                answer = temp
            # print(answer)
            return

        for i in range(len(words)):
            # print(check)
            if word_chk(words[n], words[i]) and check[i] == 0:
                # print(words[n], words[i])
                check[i] = 1
                temp += 1
                bfs(i)
                temp -= 1
                check[i] = 0
    check[0] = 1
    bfs(0)

    return 0 if answer == len(words) else answer
