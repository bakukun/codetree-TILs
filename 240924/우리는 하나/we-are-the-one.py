from collections import deque
from itertools import combinations 


n, k, u, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dxs = [1,0,-1,0]
dys = [0,1,0,-1]
size = []
cnt = 0
visited = [[False] * n for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n



# 현재 위치에서 차이나는거 몇개 갈수 있는지 카운트 
# 갈수 있는 것들 visited 반환

def bfs(x,y):
    q = deque()
    q.append((x,y))

    visited[x][y] = True
    cnt = 1

    while q:
        dx , dy = q.popleft()

        for i , j in zip(dxs,dys):
            nx = i + dx
            ny = j + dy

            if(in_range(nx,ny)):
                minus = abs(arr[dx][dy] - arr[nx][ny]) 

                if (not visited[nx][ny] and u <= minus <= d):
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return cnt


for i in range(n):
    for j in range(n):
        size.append(bfs(i,j))

size.sort(reverse=True)
        
print(sum(size[:k]))