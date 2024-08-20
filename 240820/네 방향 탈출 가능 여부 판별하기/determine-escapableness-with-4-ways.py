from collections import deque

global n,m
global collect

order = 1
q = deque()

def in_range(x,y):
    return 0 <= x and x < m and 0 <= y and y < n 

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def bfs():
    dxs = [0,0,1,-1]
    dys = [1,-1,0,0]
    
    while q:
        x,y = q.popleft();

        if x == m - 1 and y == n - 1:
            global collect
            collect = 1
            return  # 도달했으므로 탐색 종료

        for dx , dy in zip(dxs,dys):
            new_x , new_y = x+dx , y+dy

            if can_go(new_x,new_y):
                push(new_x,new_y)
            

def push(x,y):
    global order
    answer[x][y] = order
    order +=1
    visited[x][y] = True
    q.append((x,y))



n,m = map(int,(input().split()))
grid = [list(map(int,(input().split()))) for _ in range(n)]
visited = [[False for  _ in range(n)] for _ in range(n)]
answer = [[0 for  _ in range(n)] for _ in range(n)]
collect = 0

push(0,0)
bfs()
print(collect)