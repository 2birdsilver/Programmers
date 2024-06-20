import heapq

def solution(s):
    # 문자열 맨 앞,뒤의 {} 제거
    s = s[1:len(s)-2]
    answer = []

    # }, 을 구분자로 리스트형태로 나누기
    s = s.split('},')

    # 리스트 각 원소별 '{' 제거해서 집합으로 변경
    q = []
    for i in s:
        i = i[1:]
        i = set(map(int,i.split(',')))
        heapq.heappush(q, (len(i),i))

    while q:
        priority_set = heapq.heappop(q)
        priority_set = priority_set[1]

        answer.extend([i for i in priority_set if answer.count(i) == 0])


    return answer