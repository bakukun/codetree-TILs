n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
maxi = 0

for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for k in range(3):
            for l in range(3):
                tmp += arr[i+k][j+l]
        maxi = max(maxi,tmp)
        
print(maxi)