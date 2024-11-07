n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0

if(m>1):
    for i in range(len(arr)):
        cnt = 0 
        for j in range(1,len(arr)):
            if(arr[i][j-1] == arr[i][j]):
                if(cnt == 0):
                    cnt += 2
                else:
                    cnt += 1
            else:
                cnt = 0
        if (cnt >= m):
            ans += 1   

    for i in range(len(arr)):
        cnt = 0 
        for j in range(1,len(arr)-1):
            if(arr[j-1][i] == arr[j][i]):
                if(cnt == 0):
                    cnt += 2
                else:
                    cnt += 1
            else:
                cnt = 0
        if (cnt >= m):
            ans += 1   
    print(ans)  
else:
    print(n*2)