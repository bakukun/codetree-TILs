import deque from collection

a = deque()
n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [list(False for _ in range(n)) for _ in range(n)]
position = [list(map(int,input().split())) for _ in range(k)] # 1개씩 작게 설정
ans = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and arr[x][y] == 0 and check[x][y]