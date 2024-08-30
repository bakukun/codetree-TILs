n = int(input())
nums = list(map(int,input().split()))
sorted_nums = sorted(nums)
cnt = 0

while(nums != sorted_nums):
    remove = nums.pop(0)
    #print(remove)
    loop = 0
    for i in range(len(nums)-1,0,-1):
        if(nums[i] > nums[i-1]):
            loop+=1
    nums.insert(1+loop, remove)
    cnt +=1
    #print(loop,nums)


print(cnt)