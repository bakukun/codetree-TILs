def is_range(x,y):
    return 0 <= x < N and 0 <= y < N

def backtrack(n):

    global answer,cnt
    if(answer):
        x , y = answer[-1]

        tmp_dir = dir_arr[x][y]
        num = arr[x][y]
        dx , dy = dxs[tmp_dir-1] , dys[tmp_dir-1]
        #print(x,y,num,"|",dx,dy,n,"||",answer)

        for i in range(1,N):
            nx , ny = x + (i*dx) , y + (i*dy) 
            #print(x,y,nx,ny)
            if(is_range(nx,ny) and arr[nx][ny] > num):
                answer.append([nx,ny])
                backtrack(n+1)
                answer.pop()
    
    cnt = max(cnt,len(answer))
    return

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
dir_arr = [list(map(int,input().split())) for _ in range(N)]

x, y = map(int,input().split())
x, y = x - 1, y - 1

answer = []
answer.append([x,y])

dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]
cnt = 0

backtrack(0)

print(cnt-1)