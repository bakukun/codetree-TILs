def backtrack(n):

    global mini,current_location

    if current_location == N-1:
        mini = min(mini,n)
        return

    for i in range(1,arr[current_location]+1):
        if (current_location+i <= N-1):
            current_location += i
            backtrack(n+1)
            current_location -= i
    return

N = int(input())
arr = list(map(int,input().split()))
ans = []
mini = 10000
current_location = 0
backtrack(0)
if (mini == 10000):
    print(-1)
else:
    print(mini)