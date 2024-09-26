def backtracking(num):
    if num == n:
        print_k()
        return

    for i in range(1,k+1):
        if(num >=2 and ans[-1] == i and ans[-2] == i):
            continue
        ans.append(i)
        backtracking(num+1)
        ans.pop()

def print_k():
    for i in range(len(ans)):
        print(ans[i],end=" ")
    print()


k,n = map(int,input().split())
ans = []
backtracking(0)