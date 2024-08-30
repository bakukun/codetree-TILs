n = int(input())

# 배열 입력받기
arr = list(map(int,input().split()))

cnt = n - 1
while cnt >= 1:
    if arr[cnt] < arr[cnt - 1]:
        break
    cnt -= 1

print(cnt)