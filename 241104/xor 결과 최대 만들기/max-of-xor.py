def xor(ans):
    tmp = ans[0]
    for i in range(1,len(ans)):
        tmp = tmp ^ ans[i]
    return tmp

def backtracking(cnt):
    if(cnt == M):
        maxi = max(maxi,xor(ans))
        return
    
    for i in range(arr):
        ans.append(i)
        backtracking(cnt+1)
        ans.pop()

        backtracking(cnt)


N,M = map(int,input().split())
arr = list(map(int,input().split())
ans = []
maxi = 0
backtracking(0)