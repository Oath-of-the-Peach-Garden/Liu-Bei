# 시저암호
def solution(s, n):
    answer = ''
    for ch in s:
        ascii = ord(ch)
        # print(ascii)
        if ((ascii in range(65,91)) and ascii+n>90) or ((ascii in range(97,123)) and ascii+n>122):
            ascii = ascii - 26
        temp = chr(ascii+n)
        if ch == ' ': temp = ' '
        # print(temp)
        answer += temp
    return answer