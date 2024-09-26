def position_check(tmp_row):
    tmp_position = start_position[:]
    for i in range(len(tmp_row)):
        switch = tmp_row[i][0]
        tmp_position[switch-1] , tmp_position[switch] = tmp_position[switch] , tmp_position[switch-1]
    return tmp_position

def init_position():
    for i in range(1,n+1):
        start_position.append(i)

def backtracking(start, num, add_row):
    
    global minimum

    if (position_check(add_row) == position):  
        minimum = min(minimum, len(add_row))
        return
    
    if(num == len(row_arr)):
        return
    
    for i in range(start,len(row_arr)):
        add_row.append(row_arr[i])
        backtracking(i+1,num+1,add_row)
        add_row.pop()

    return


n,m = map(int,input().split())
row_arr = [list(map(int,input().split())) for _ in range(m)]
row_arr.sort(key=lambda x:x[-1])
position = []
start_position = []

ans_row = []
add_row = []
minimum = m

init_position()
position = position_check(row_arr)
backtracking(0,0,add_row)

print(minimum)