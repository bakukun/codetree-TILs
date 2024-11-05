def backtracking(idx,cnt):
    global ans,mini

    if cnt == N:
        other = list(set_nlist - set(ans))

        if(len(other) == len(ans)):
            mini = min(mini,abs(sum(ans)-sum(other)))
        return

    if(idx == len(n_list)-1):
        return

    
    ans.append(n_list[idx])
    backtracking(idx,cnt+1)
    ans.pop()
    
    backtracking(idx+1,cnt)


        
N = int(input())
n_list = list(map(int,input().split()))
set_nlist = set(n_list)
ans = []
mini = 10000000000
backtracking(0,0)
print(mini)