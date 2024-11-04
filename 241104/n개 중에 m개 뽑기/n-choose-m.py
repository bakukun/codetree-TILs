def print_permutation(ans):
    for i in ans:
        print(i,end=" ")
    print()


def backtrack(curr_n,n):
    global ans

    if(curr_n == N+1):
        if (n == M):
            print_permutation(ans)
        return

    ans.append(curr_n)
    backtrack(curr_n+1,n+1)
    ans.pop()

    backtrack(curr_n+1,n)

        
N,M = map(int,input().split())
ans = []
backtrack(1,0)