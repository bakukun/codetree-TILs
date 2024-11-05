def backtrack(row,cnt):
    global maxi

    if cnt == n:
        tmp = 0
        for i in range(len(ans)):
            tmp += arr[i][ans[i]]
        maxi = max(tmp,maxi)
        return

    if row >= n:
        return

    for col in range(n): #모든 열 검사
        if not visited[col]:  # 열 방문 체크
            visited[col] = True
            ans.append(col) 
            backtrack(row + 1, cnt + 1)
            ans.pop()
            visited[col] = False

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
ans = []
maxi = 0

backtrack(0,0)

print(maxi)