from collections import deque
from math import ceil


def solution(progresses, speeds):
    answer = []
    periods = []

    # 각 기능별 소요일수 계산해서 리스트에 저장
    for i in range(len(progresses)):
        period = ceil((100-progresses[i])/speeds[i])
        periods.append(period)

    q = deque(periods)
    while q:
        standard = q.popleft()
        count = get_distribution_count(standard, q)
        answer.append(count)

    return answer

# 배포가능한 기능수를 반환하는 함수
def get_distribution_count(standard, q):
    count = 1
    while q:
        if q[0] <= standard:
            q.popleft()
            count += 1
        else:
            break
    return count