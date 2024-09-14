n = int(input())
cnt = [-1]  * (n+1)

def stair(x):
    if cnt[x] != -1:
        return cnt[x] % 10007
    if  x <= 4:
        cnt[x] = 1
    else:
        cnt[x] = (stair(x-2) + stair(x-3)) % 10007
   
    return (cnt[x])

stair(n)
print(cnt[n])