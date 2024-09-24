from collections import deque


#1. BFS 필요한 값 세팅
n , m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dxs = [1,0,-1,0]
dys = [0,1,0,-1]

#1-1. 범위 함수 세팅
def can_go(x,y): 
    return 0 <= x < n and 0 <= y < m

#2. BFS 함수 세팅 (물 범위 파악)
def bfs():

    '''
    전역 변수로 check 선언시,
    이전 탐색의 방문 기록이 남아 정확한 탐색을 방해 (다시 실행할 때 마다 초기화)
    빙하가 녹을 때마다 외부 공기와 연결된 영역이 달라지므로, 매번 새로운 check 배열 필요함
    '''
    check = [[False] * m for _ in range(n)]

    #2-1. 큐 선언 후, 초기 좌표 방문 처리
    q = deque() 
    q.append((0, 0))
    check[0][0] = True 

    #2.2. 좌표들 큐에 넣고 빼면서 확인
    while q: 
        x, y = q.popleft() # 큐 속의 현재 좌표 불러오기

        #2-3. 현재 좌표 기준 상하좌우 탐색
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            #2-4. 범위 내에 있으면서 같은 '물' 이면?
            if can_go(nx,ny):
                if check[nx][ny] == False and arr[nx][ny] == 0: 
                    check[nx][ny] = True 
                    q.append((nx, ny)) # 방문 했다고 갱신 후, BFS 다시 실행
 
    return check # 물 방문 여부 배열 리턴

time = 0 # 소요시간 
last_melt_count = 0 # 녹은 빙하의 크기

#3-1. 소요시간 및 녹은 빙하의 크기 파악 (BFS)
while True:
    
    check = bfs() # check 배열을 통해 빙하가 외부 물과 닿아있는지를 판단
    melt_list = [] # 빙하의 좌표를 넣을 리스트

    #3-2. 빙하의 좌표를 찾고 그 외부에 물 있는지 탐색
    for i in range(n): 
        for j in range(m):
            if arr[i][j] == 1: 
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if can_go(nx, ny) and arr[nx][ny] == 0 and check[nx][ny]:
                        melt_list.append((i, j)) # 녹을 빙하에 추가
                        break # 굳이 선택한 i,j 4방향 전부 안보고 다음 격자로 넘어감

    # 3-3-1. 녹을 빙하가 없다면, 출력 후 while 문 탈출
    if not melt_list:
        print(time, last_melt_count)
        break

    # 3-3-2. 녹을 빙하가 있다면, 녹을 빙하를 갱신 후, while 문 반복 + 시간 추가
    last_melt_count = len(melt_list)
    for x, y in melt_list:
        arr[x][y] = 0
    time += 1