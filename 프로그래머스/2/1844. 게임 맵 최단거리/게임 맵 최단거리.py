from collections import deque

def solution(maps):
    n = len(maps) # 행 수
    m = len(maps[0]) # 열 수

    visited = [[False for i in range(m)] for j in range(n)] # 방문여부 체크 테이블

    directions = []
    directions.append((0,1)) # 오른쪽
    directions.append((1,0)) # 아래쪽
    directions.append((-0, -1)) # 왼쪽
    directions.append((-1, 0)) # 위쪽

    que = deque()
    que.append((0,0)) # 시작지점 추가

    while que:
        x, y = que.popleft()
        for direction in directions:
            dx, dy = direction
            nx = x + dx
            ny = y + dy

            if (0 <= nx < n and 0 <= ny < m):
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True # 방문
                    maps[nx][ny] = maps[x][y] + 1 # 이전 방문 스팟 수 + 1
                    que.append((nx, ny))

    # 현재 지점에서 동,서,남,북 모든 방향으로 이동 불가한 경우
    if (visited[n-1][m-1] == False): # 목적지가 벽이여서 접근 불가한 경우
        return -1
    else:
        return maps[n-1][m-1] # 목적지에 도달한 경우