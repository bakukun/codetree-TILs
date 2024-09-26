n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
line = []
select_line = []

def is_overlap(x1,y1,x2,y2):
    if (x1 <= x2 <= y1 or x1 <= y2 <= y1 or x2 <= x1 <= y2 or x2 <= y1 <= y2):
        return True
    return False

def check(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                x1, y1 = arr[i]
                x2, y2 = arr[j]
                if is_overlap(x1,y1,x2,y2):
                    return False
                
    return True

def backtracking(num):
    if num == n:
        if (check(select_line)):
            line.append(len(select_line))
        return

    select_line.append(arr[num])
    backtracking(num+1)
    select_line.pop()
    backtracking(num+1)

backtracking(0)

print(max(line))