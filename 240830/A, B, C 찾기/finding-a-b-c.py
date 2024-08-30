arr = list(map(int,input().split()))
arr.sort()
minimum_a = arr[0]
minimum_b = arr[1]
minimum_c = arr[len(arr)-1] - minimum_a - minimum_b

print(minimum_a,minimum_b,minimum_c)