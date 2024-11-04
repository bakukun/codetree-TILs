def xor(ans):
    tmp = ans[0]
    for i in range(1, len(ans)):
        tmp = tmp ^ ans[i]
    return tmp


def backtracking(idx,cnt):
    global ans,maxi
    if (cnt == M):
        maxi = max(maxi, xor(ans))
        return

    for i in range(idx,len(arr)):
        ans.append(arr[i])
        backtracking(i+1,cnt + 1)
        ans.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
maxi = 0
backtracking(0,0)
print(maxi)