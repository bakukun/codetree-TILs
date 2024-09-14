n = int(input())
cnt = [-1]  * (n+1)

def stair(x):
    if cnt[x] != -1:
        return cnt[x] 
    if 2 <= x and x <= 3:
        cnt[x] = 1
    else:
        cnt[x] = cnt[x-2] + cnt[x-3]
     
    return(cnt[x])

stair(n)
print(cnt[n])