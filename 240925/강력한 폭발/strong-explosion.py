bomb_1 = [(0,-2),(0,-1),(0,1),(0,2)]
bomb_2 = [(1,0),(0,1),(-1,0),(0,-1)]
bomb_3 = [(1,1),(-1,1),(-1,-1),(1,-1)]


# 1. 입력 값 받기
n = int(input())
bomb_list = [list(map(int,input().split())) for _ in range(n)]
bomb_m = [[0 for _ in range(n)] for _ in range(n)] #폭탄 최대 터질 곳
bomb_idx = [] # 폭탄 위치
bomb_count = 0 # 폭탄 개수
ans = []
arr = []

def bomb_init():
    bomb_m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(bomb_idx)):
        bomb_m[bomb_idx[i][0]][bomb_idx[i][1]] = 1
    return bomb_m


def choose(num):
    if num == bomb_count:
        bomb(arr)
        return
    else:
        for i in range(1,4):
            arr.append(i)
            choose(num+1)
            arr.pop()
    return 

def bomb(arr):
    bomb_m = bomb_init()
    cnt = bomb_count

    for idx in range(len(arr)):
        
        x = bomb_idx[idx][0] 
        y = bomb_idx[idx][1]

        bomb_type = arr[idx]

        if (bomb_type == 1):
            for dx,dy in bomb_1:
                nx = dx + x
                ny = dy + y
                if ( 0 <= nx < n and 0 <= ny < n):
                    if ( bomb_m[nx][ny] == 0 ):
                        bomb_m[nx][ny] = 1
                        cnt += 1
        if (bomb_type == 2):
            for dx,dy in bomb_2:
                nx = dx + x
                ny = dy + y
                if ( 0 <= nx < n and 0 <= ny < n):
                    if ( bomb_m[nx][ny] == 0 ):
                        bomb_m[nx][ny] = 1
                        cnt += 1
        if (bomb_type == 3):
            for dx,dy in bomb_3:
                nx = dx + x
                ny = dy + y
                if ( 0 <= nx < n and 0 <= ny < n):
                    if ( bomb_m[nx][ny] == 0 ):
                        bomb_m[nx][ny] = 1
                        cnt += 1

    ans.append(cnt)


for i in range(n):
    for j in range(n):
        if (bomb_list[i][j] == 1):
            bomb_idx.append((i,j))
            bomb_m[i][j] = 1 
            bomb_count += 1
 
choose(0)
print(max(ans))