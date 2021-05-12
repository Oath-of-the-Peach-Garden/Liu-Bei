# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ""

    keys = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "*": (3, 0), "0": (3, 1), "#": (3, 2),
    }
    left = keys["*"]
    right = keys["#"]

    for number in numbers:
        number = str(number)

        if number in ("1", "4", "7"):
            answer += "L"
            left = keys[number]
        elif number in ("3", "6", "9"):
            answer += "R"
            right = keys[number]
        else:
            num_pos = keys[number]
            left_dist = abs(left[0]-num_pos[0]) + abs(left[1]-num_pos[1])
            right_dist = abs(right[0]-num_pos[0]) + abs(right[1]-num_pos[1])
            if left_dist == right_dist:

                if hand == "left":
                    left = num_pos
                    answer += "L"
                elif hand == "right":
                    right = num_pos
                    answer += "R"

            elif right_dist < left_dist:
                answer += "R"
                right = num_pos
            else:
                answer += "L"
                left = num_pos

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
