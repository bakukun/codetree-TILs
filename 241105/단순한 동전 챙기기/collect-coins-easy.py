def calc_dist(a, b): # 두 포인트의 거리 구하기
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def backtrack(idx,cnt):
    global ans, mini
    #print(ans,idx,cnt)
    #코인 종류 3개시, mini 갱신
    if (cnt == 3):
        tmp = 0
        tmp += calc_dist(startpoint,coin_dict[ans[0]])
        for i in range(0,2):
            tmp += calc_dist(coin_dict[ans[i]],coin_dict[ans[i+1]])
        tmp += calc_dist(endpoint,coin_dict[ans[-1]])
        mini = min(mini, tmp)
        return

    # 모든 코인을 다 확인했으면 종료
    if idx == len(coin):
        return

    ans.append(coin[idx]) # idx에 따라 coin에 맞는 동전을 갖고 오고, 이를 ans에 저장
    backtrack(idx+1, cnt+1) # 현재 coin 추가하고 가지치기
    ans.pop()

    backtrack(idx+1, cnt) # 현재 coin 추가 안하고 가지치기


N = int(input())
arr = [list(input()) for _ in range(N)]
coin = [] # 동전의 종류 저장
coin_dict = dict() # 동전의 종류에 맞게 좌표 저장

startpoint = [] #시작점
endpoint = [] #종료점

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 'S':
            startpoint.append(i)
            startpoint.append(j)
        if arr[i][j] == 'E':
            endpoint.append(i)
            endpoint.append(j)
        if '1' <= arr[i][j] <= '9':
            coin.append(int(arr[i][j])) #동전 종류 저장
            coin_dict[int(arr[i][j])] = (i, j) #동전 좌표 저장

coin.sort() # 오름차순 정렬

ans = []
mini = 10000000

#idx -> coin 배열 내에서
# n개 중에 m개 뽑도록 백트래킹 도와주는 idx

backtrack( 0, 0)
if (mini == 10000000):
    print(-1)
else:
    print(mini)