def backtracking(idx,cnt):
    global ans,mini

    if cnt == N:

        other = []

        n_visited = [False] * len(n_list)

        for num in ans:
            for j in range(len(n_list)):
                if num == n_list[j] and n_visited[j] == False:
                    n_visited[j] = True
                    break

        for i in range(len(n_visited)):
            if(n_visited[i] == False):
                other.append(n_list[i])

        #print(ans,other)
        mini = min(mini,abs(sum(ans)-sum(other)))
        return 

    if(idx == len(n_list)-1):
        return

    
    ans.append(n_list[idx])
    backtracking(idx+1,cnt+1)
    ans.pop()
    
    backtracking(idx+1,cnt)


        
N = int(input())
n_list = list(map(int,input().split()))


ans = []
mini = 10000000000
backtracking(0,0)
print(mini)