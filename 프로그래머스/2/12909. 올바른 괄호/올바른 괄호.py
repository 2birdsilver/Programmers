def solution(s):

    answer = 0
    for i in range(0, len(s)):
        if answer < 0:
            return False

        if s[i] == "(":
            answer += 1
        else:
            answer -= 1

    return True if answer == 0 else False