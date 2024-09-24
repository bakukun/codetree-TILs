from collections import deque

n , m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
print(check)
dxs = [1,0,-1,0]
dys = [0,1,0,-1]

def can_go(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(): # 물 파악 하는 BFS
    q = deque() # 큐 선언
    q.append((0, 0)) # 0,0 삽입 및 방문 처리
    check[0][0] = True 

    while q: # 큐에 넣고 빼면서 확인
        x, y = q.popleft() # 현재 좌표 빼기
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            print(nx,ny)
            if can_go(dx,dy):
                print("can_go?",nx,ny)
                if check[nx][ny] == False and arr[nx][ny] == 0: # 갈 수 있으면서 '물'이면?
                    check[nx][ny] = True # 방문 했다고 갱신하고 
                    q.append((nx, ny)) # 물인 곳 추가
    return check

time = 0 # 소요시간 
last_melt_count = 0

# 소요시간 파악
while True:
    check = bfs() # 물이 있는 check 배열 불러오기
    melt_list = [] # 빙하의 좌표를 넣을 리스트
    for i in range(n): 
        for j in range(m):
            if arr[i][j] == 1: # 빙하의 좌표를 찾고 그 외부에 물 있는지 탐색
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if can_go(nx, ny) and arr[nx][ny] == 0 and visited[nx][ny]:
                        melt_list.append((i, j)) #녹을 빙하에 추가
                        break
    if not melt_list:
        print(time, last_melt_count)
        break
    last_melt_count = len(melt_list)
    for x, y in melt_list:
        arr[x][y] = 0
    time += 1


print(time,last_melt_count)