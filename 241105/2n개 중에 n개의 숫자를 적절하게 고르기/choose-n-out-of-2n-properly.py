def backtracking(idx,cnt):
    global ans,mini

    if cnt == N:

        other = []
        n_visited = [False] * len(n_list)
        sum_ans = 0
        sum_other = 0

        for n_idx in ans:
            n_visited[n_idx] = True
            sum_ans += n_list[n_idx]

        for i in range(len(n_visited)):
            if not n_visited[i]:
                sum_other += n_list[i]

        #print(ans,other)
        mini = min(mini,abs(sum_ans-sum_other))
        return 

    if(idx == len(n_list)-1):
        return

    
    ans.append(idx)
    backtracking(idx,cnt+1)
    ans.pop()
    
    backtracking(idx+1,cnt)


        
N = int(input())
n_list = list(map(int,input().split()))


ans = []
mini = 10000000000
backtracking(0,0)
print(mini)