# 완주하지 못한 선수
# 해시

# 아닌거 같긴했는데 역시나 아니었다!
# 효율성0점나옴
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()


    for player in participant:
        if player not in completion:
            answer = player
            break
        if participant.count(player) > 1 and participant.count(player) != completion.count(player):
            answer = player
            break

    return answer

# 배열을 정렬해서 둘이 다르면 결과값리턴
def solution2(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    # print(f'{participant[len(participant)]}')

    # 리스트 두개의 길이가 다르면 짧은 쪽에 맞춰서 인덱스가 넘어가지 않음?
    # for player, c_player in zip(participant, completion):
    #     print(f'{player}, {c_player}')
    #     if player != c_player:
    #         answer = player
    #         break

    # 되긴 되는데 어쩌다보니 자바 풀이를 봐버리고 풀어서 찜찜함
    for i in range(len(participant)):
        if len(completion) == i or participant[i] != completion[i]:
           answer = participant[i]
           break

    return answer

def solution3(participant, completion):
    answer = ''
    # print(len(list(set(participant))), len(participant))
    if len(list(set(participant))) == len(participant):
        answer = list(set(participant) - set(completion))

    for player in participant:
        if player not in completion:
            answer = player
            break


    return answer

def solution4(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    while 1:
        start = 0
        end = len


    return answer

print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))
print("두번째",solution2(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))
print("두번째",solution2(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['josipa', 'filipa', 'marina', 'nikola']))

print(solution3(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))

