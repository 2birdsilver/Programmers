from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)

    for i in permutations(dungeons, n):
        count = 0
        fatigue = k

        for dungeon in i:
            if fatigue < dungeon[0]:
                break
            count += 1
            fatigue -= dungeon[1]

        answer = max(answer, count)

    return answer