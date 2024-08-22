from collections import deque 

n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [list(False for _ in range(n)) for _ in range(n)]
answer = [list(0 for _ in range(n)) for _ in range(n)]
position = [list(map(int,input().split())) for _ in range(k)] # 1개씩 작게 설정
order = 0
q = deque()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and arr[x][y] == 0 and check[x][y] == False

def bfs():
    dxs , dys = [1,0,-1,0], [0,-1,0,1]
    while q:
        x,y = q.popleft()
        
        for dx , dy in zip(dxs,dys):
            new_x , new_y  = x + dx , y + dy

            if can_go(new_x,new_y):
                push(new_x,new_y)

def push(x,y):
    global order
    answer[x][y] = order
    order +=1
    check[x][y] = True
    q.append((x,y))

for x,y in position:
    start_x , start_y = x-1 , y-1
    if(check[start_x][start_y] == False):
        push(start_x,start_y)
        bfs()

print(order)