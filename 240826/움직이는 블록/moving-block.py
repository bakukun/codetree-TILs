n = int(input())
nums = []
add = 0
ans = 0
min_gap = 10001

for _ in range(n):
    a = int(input())
    nums.append(a)
    add += a
    
avg = add // n

maximum = 0
minimum = 0
for num in nums:
    if num > avg:
        maximum += (num - avg)
    elif num < avg:
        minimum += (avg - num)

print(maximum)