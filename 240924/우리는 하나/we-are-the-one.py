from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

coords = [(i, j) for i in range(n) for j in range(n)]
start_positions = list(combinations(coords, k))

maximum = 0

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    diff = abs(arr[cx][cy] - arr[nx][ny])
                    if u <= diff <= d:
                        visited[nx][ny] = True
                        count += 1
                        q.append((nx, ny))
    return count

for starts in start_positions:
    visited = [[False]*n for _ in range(n)]
    total_cells = 0
    valid = True
    for x, y in starts:
        if visited[x][y]:
            # 시작 위치가 이미 방문되었으면 이 조합은 유효하지 않음
            valid = False
            break
        else:
            count = bfs(x, y, visited)
            total_cells += count
    if valid:
        maximum = max(maximum, total_cells)

print(maximum)