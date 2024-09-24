from collections import deque
from itertools import combinations 

n, k, u, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dxs = [1,0,-1,0]
dys = [0,1,0,-1]
cnt = 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n



# 현재 위치에서 차이나는거 몇개 갈수 있는지 카운트 
# 갈수 있는 것들 visited 반환

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[False] * n for _ in range(n)]
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
    return visited, cnt


def bfs2(x,y,visited):
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
    return visited, cnt

maximum = 0


coords = [(i, j) for i in range(n) for j in range(n)]
comb = list(combinations(coords, k))


for num in comb:
    if(k == 1):
        x , y = num[0]
        visited , tmp = bfs(x,y)
        maximum = max(maximum,tmp)
    elif(k == 2):
        x1 , y1 = num[0]
        x2 , y2 = num[1]
        visited , tmp = bfs(x1,x2) 
        visited , tmp2 = bfs2(x2,y2,visited)
        maximum = max(maximum, tmp + tmp2)
    else:
        x1 , y1 = num[0]
        x2 , y2 = num[1]
        x3 , y3 = num[2]
        visited , tmp = bfs(x1,x2) 
        visited , tmp2 = bfs2(x2,y2,visited)
        visited , tmp3 = bfs3(x3,y3,visited)
        maximum = max(maximum,  tmp + tmp2 + tmp3)
        
print(maximum)