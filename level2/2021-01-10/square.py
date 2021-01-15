# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
# https://hocheon.tistory.com/93
def solution(w, h):
    if w == h:
        return w * h - w

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    if w > h:
        l = w
        s = h
    else:
        l = h
        s = w

    g = gcd(l, s)
    return w * h - (w+h-g)
