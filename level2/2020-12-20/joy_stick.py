# 조이 스틱
import re


def solution(name):
    answer = 0
    change = 0
    move1 = 0

    for letter in name:
        code = ord(letter)
        if 90 - code > code - 65:
            change += code - 65
        else:
            change += 91 - code
        if letter != "A":
            move1 += 1
    move1 -= 1

    p = re.compile('[A]+')
    move2 = p.findall(name)
    print(len(max(move2)) if move2 else 0)

    answer = change + move1

    return answer


# 푼 것

def solution2(name):
    name = list(name)
    total = 0
    i = 0

    while True:
        # 상하
        total += min(ord(name[i])-65, 91-ord(name[i]))
        name[i] = 'A'

        if name.count('A') == len(name):
            return total

        # 좌우
        right, left = 1, 1
        for m in range(1, len(name)):
            if name[i+m] == 'A':
                right += 1
            else:
                break
        for m in range(1, len(name)):
            if name[i-m] == 'A':
                left += 1
            else:
                break

        if left < right:
            i -= left
            total += left
        else:
            i += right
            total += right
