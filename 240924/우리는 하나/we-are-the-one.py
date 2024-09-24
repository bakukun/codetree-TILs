from collections import deque

n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

visited = [[False] * n for _ in range(n)]
component_sizes = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        dx, dy = q.popleft()

        for i, j in zip(dxs, dys):
            nx = dx + i
            ny = dy + j

            if in_range(nx, ny) and not visited[nx][ny]:
                diff = abs(arr[dx][dy] - arr[nx][ny])
                if u <= diff <= d:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return cnt

# Find all connected components
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = bfs(i, j)
            component_sizes.append(size)

# Get the sum of the sizes of the largest k components
component_sizes.sort(reverse=True)
maximum = sum(component_sizes[:k])

print(maximum)