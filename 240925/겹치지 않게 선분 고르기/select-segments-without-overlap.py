n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
line = []
select_line = []

def check():
    endPoint = 0
    tmp_line = arr
    tmp = 0
    tmp_line.sort(key=lambda x: (x[1], x[0]))
    
    for start , end in tmp_line:
        if endPoint < start:
            tmp += 1
            endPoint = end
    return tmp

print(check())