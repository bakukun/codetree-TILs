n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
line = []
select_line = []
ans = 0

def check():
    endPoint = 0
    tmp_line = select_line
    tmp = 0
    tmp_line.sort(key=lambda x: (x[1], x[0]))

    for start , end in tmp_line:
        if endPoint <= start:
            tmp += 1
            endPoint = end
    return tmp


def choose(num):
    global ans
    if(num == n):
        ans = max(ans,check())
        return
    
    select_line.append(arr[num])
    choose(num+1)
    select_line.pop()
    choose(num+1)

choose(0)

print(ans)