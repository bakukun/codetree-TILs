n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
maximum = max(arr)
minimum = min(arr)


if (maximum[1] - maximum[0] > minimum[1] - minimum[0]):
    arr.remove(maximum)
else:
    arr.remove(minimum)


print(max(arr)[1]-min(arr)[0])