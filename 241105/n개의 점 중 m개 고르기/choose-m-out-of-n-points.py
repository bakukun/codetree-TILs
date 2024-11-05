def distance(d1,d2):
    d1x, d1y = d1[0], d1[1]
    d2x, d2y = d2[0], d2[1]
    return (d1x - d2x)**2 + (d1y - d2y)**2

def backtrack(idx,cnt):
    global ans,mini
    if cnt == m:
        maxi_tmp = 0
        for i in range(len(ans)-1):
            for j in range(i+1,len(ans)):
                tmp = distance(arr[ans[i]],arr[ans[j]])
                maxi_tmp = max(maxi_tmp,tmp)
        mini = min(maxi_tmp,mini)
        return
    
    if idx == len(arr):
        return

    ans.append(idx)
    backtrack(idx+1,cnt+1)
    ans.pop()
    backtrack(idx+1,cnt)



n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
mini = 10000000000
ans = [] #index 삽입
backtrack(0,0)
print(mini)