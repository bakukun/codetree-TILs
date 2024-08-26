n = int(input())
num = []
add = 0
min_gap = 10001

for _ in range(n):
    a = int(input())
    num.append(a)
    add += a
    
avg = add // n


for i in range(n):
    tmp = num[i]
    if ( min_gap > min(min_gap,abs(tmp-avg))):
        min_gap = abs(tmp-avg)
        idx = i
        
print(num[idx])