def calc_dist(a, b): # 두 포인트의 거리 구하기
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def backtrack(idx,cnt):
    global ans, mini

    if (cnt == 3):
        tmp = 0
        tmp += calc_dist(startpoint,coin_dict[ans[0]])
        for i in range(0,2):
            tmp += calc_dist(coin_dict[ans[i]],coin_dict[ans[i+1]])
        tmp += calc_dist(endpoint,coin_dict[ans[-1]])
        mini = min(mini, tmp)
        return

    if idx == len(coin):
        return

    ans.append(coin[idx])
    backtrack(idx+1, cnt+1)
    ans.pop()

    backtrack(idx+1, cnt)



N = int(input())
arr = [list(input()) for _ in range(N)]
coin_dict = dict()
coin = []
startpoint = []
endpoint = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 'S':
            startpoint.append(i)
            startpoint.append(j)
        if arr[i][j] == 'E':
            endpoint.append(i)
            endpoint.append(j)
        if '1' <= arr[i][j] <= '9':
            coin.append(int(arr[i][j]))
            coin_dict[int(arr[i][j])] = (i, j)

coin.sort()

ans = []
mini = 10000000

backtrack( 0, 0)
if (mini == 10000000):
    print(-1)
else:
    print(mini)