def  backtracking(n):
    global cnt

    if n == N:
        cnt = max(cnt,max_cnt(answer))
        return

    for i in range(K):
        answer.append(arr[i])
        backtracking(n+1)
        answer.pop()
    

def max_cnt(answer):
    #print()
    move_cnt = 0
    tmp_cnt = [0 for _ in range(K)]

    for i in range(len(answer)):
        tmp_cnt[answer[i]-1] += move[i]

    #print(tmp_cnt)    

    for i in range(len(tmp_cnt)):
        if (tmp_cnt[i] >= M-1):
            move_cnt += 1

    return move_cnt



N,M,K = map(int,input().split())
move = list(map(int,input().split()))
answer = []
arr = [i for i in range(1,K+1)]
cnt = 0
backtracking(0)
print(cnt)