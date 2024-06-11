from collections import deque

def solution(citations):
    # 최대 인용 수
    max_citation = max(citations)
    if max_citation == 0:
        return 0
    elif max_citation == 1:
        return 1
    stack = deque(citations)

    # 인용 수에 따른 논문 수 구하기
    cited_paper = [0] * (max_citation+1)

    while stack:
        citation = stack.pop()
        for i in range(citation+1):
            cited_paper[i] += 1

    # 최대 인용 수 부터 인용 수에 따른 논문 수 확인
    for h in range(max_citation, 0, -1):
        if cited_paper[h] >= h:
            return h