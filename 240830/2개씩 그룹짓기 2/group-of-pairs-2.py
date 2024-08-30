n = int(input())
arr = list(map(int,input().split()))
sa = sorted(arr)
nums = []

for i in range(0,n):
    nums.append(sa[n+i] - sa[i])

print(min(nums))