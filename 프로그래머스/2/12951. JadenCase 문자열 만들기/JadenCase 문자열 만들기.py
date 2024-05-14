def solution(s):
    answer = ''
    word = ''
    for item in s:
        if item == ' ':
            answer += word.capitalize()
            word = ""
            answer += item
        else:
            word += item

    if word != '':
        answer += word.capitalize()
    return  answer