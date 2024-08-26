from collections import deque
from itertools import combinations

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and arr[x][y] == 0

def bfs(start):
    check = [[False] * n for _ in range(n)]
    q = deque(start)
    
    # 시작 좌표를 큐와 체크 배열에 추가
    for x, y in start:
        check[x][y] = True

    reachable_cells = 0
    while q:
        now_x, now_y = q.popleft()
        reachable_cells += 1
        
        for dx, dy in zip(dxs, dys):
            nx, ny = now_x + dx, now_y + dy
            if can_go(nx, ny) and not check[nx][ny]:
                q.append((nx, ny))
                check[nx][ny] = True

    return reachable_cells

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start = [list(map(int, input().split())) for _ in range(k)]
start = [[x - 1, y - 1] for x, y in start]
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

# 바위의 위치를 저장
stone_positions = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 1]
max_reachable = 0

# 바위를 제거할 조합 생성
for rocks_to_remove in combinations(stone_positions, m):
    # 바위를 제거
    for x, y in rocks_to_remove:
        arr[x][y] = 0
    
    # BFS를 통해 도달 가능한 셀의 수를 계산
    reachable = bfs(start)
    max_reachable = max(max_reachable, reachable)
    
    # 바위를 원상복구
    for x, y in rocks_to_remove:
        arr[x][y] = 1

print(max_reachable)