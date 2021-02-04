# # 가장 긴 팰린드롬
# # https://programmers.co.kr/learn/courses/30/lessons/12904

# # 시간 초과
# from collections import deque


# def solution(s):
#     answer = 0
#     flag = False
#     for length in range(len(s)-1, -1, -1):
#         start = 0
#         last = 0
#         while last < len(s):
#             last = start + length + 1
#             # print(s[start:last])
#             if list(s[start:last]) == list(reversed(s[start:last])):
#                 answer = length+1
#                 flag = True
#                 break
#             start += 1
#         if flag:
#             break

#     return answer


# # 시간초과


# def solution(s):
#     answer = 0
#     flag = False
#     for i in range(len(s), 0, -1):
#         queue = deque(s)
#         for _ in range(0, len(s)-i+1):
#             temp = list(queue)[:i]
#             start = 0
#             end = len(temp)-1
#             for _ in range(len(temp)//2):
#                 # print(temp, temp[start], temp[end])
#                 if temp[start] != temp[end]:
#                     break
#                 start += 1
#                 end -= 1
#             else:
#                 answer = i
#                 flag = True
#             queue.append(queue.popleft())
#         if flag:
#             break
#     return answer

def solution(s):
    answer = 0
    for length in range(len(s)-1, -1, -1):
        start = 0
        end = 0
        while end < len(s):
            end = start + length + 1
            # print(s[start:last])
            if answer > length:
                return answer
            temp = list(s[start:end])
            t_start = 0
            t_end = len(temp) - 1
            for _ in range(len(temp)//2):
                if temp[t_start] != temp[t_end]:
                    break
                t_start += 1
                t_end -= 1
            else:
                answer = length+1
            start += 1

    return answer


print(solution('abcdcba'))
print(solution('abacde'))

# slice 최고...


def solution_fin(s):
    answer = 0
    for length in range(len(s)-1, -1, -1):
        start = 0
        end = 0
        while end < len(s):
            end = start + length + 1
            if s[start:end] == (s[start:end])[::-1]:
                return length+1

            start += 1

    return answer
