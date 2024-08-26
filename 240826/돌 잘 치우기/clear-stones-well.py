from collections import deque
from itertools import combinations

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y):
    return in_range(x,y) and arr[x][y] == 0

def bfs(start):

    for i in range(k):
        tmp = 0

        check = [[False] * n for _ in range(n)]
        q = deque(start)

        for x, y in start:
            check[x][y] = True
        
        while q:
            now_x , now_y = q.popleft() 
            tmp+=1

            for j in range(4):
                nx , ny = now_x + dxs[j] , now_y + dys[j]

                if can_go(nx,ny) and not check[nx][ny]:
                    q.append([nx,ny])
                    check[nx][ny] = True
    return tmp



n,k,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
start = [list(map(int,input().split())) for _ in range(k)]
start = [[x - 1, y - 1] for x, y in start]
dxs , dys = [1,-1,0,0] , [0,0,1,-1]
max_reachable = 0



stone_positions = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 1]
for rocks_to_remove in combinations(stone_positions,m):
    for x, y in rocks_to_remove:
        arr[x][y] = 0
    reachable = bfs(start)
    max_reachable = max(max_reachable, reachable)

    for x, y in rocks_to_remove:
        arr[x][y] = 1



print(max_reachable)