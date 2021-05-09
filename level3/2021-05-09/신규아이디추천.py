# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410
def remove_jum(string):
    while string.startswith('.'):
        string = string[1:]
    while string.endswith('.'):
        string = string[:-1]
    return string


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    check = ''

    for i in range(len(new_id)):
        ch = new_id[i]
        if (48 <= ord(ch) <= 57 or 97 <= ord(ch) <= 122 or ch in ['-', '_', '.']):
            check += ch
        # print(check)

    check_id = ''
    pre = ''
    for i in range(len(check)):
        ch = check[i]
        if pre != '.' or ch != '.':
            check_id += ch
        pre = ch
        # print(check_id)

    check_id = remove_jum(check_id)

    if check_id == '':
        check_id = 'a'

    if len(check_id) > 15:
        check_id = check_id[:15]

    check_id = remove_jum(check_id)

    if len(check_id) <= 2:
        check_id += check_id[-1] * (3-len(check_id))

    return check_id
