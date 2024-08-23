from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

r -= 1 
c -= 1 

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

ans_x = r
ans_y = c

for _ in range(k):
    visited = [[False]*n for _ in range(n)]
    max_num = 0
    q = deque()
    q.append([ans_x, ans_y])
    visited[ans_x][ans_y] = True

   # bfs
    while q:
        now_x, now_y = q.popleft()

        for i in range(4):
            nx = now_x + dxs[i]
            ny = now_y + dys[i]

            if in_range(nx,ny):

                if not visited[nx][ny] and arr[nx][ny] < arr[r][c]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    
                    if arr[nx][ny] > max_num:
                        max_num = arr[nx][ny]
                        ans_x, ans_y = nx, ny
                    
                    elif arr[nx][ny] == max_num:
                        if ans_x > nx:
                            ans_x, ans_y = nx, ny
                        elif ans_x == nx:
                            if ans_y > ny:
                                ans_x, ans_y = nx, ny

    r = ans_x
    c = ans_y

print(ans_x+1,ans_y+1)