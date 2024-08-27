n = int(input())
num = list(map(int,input().split()))
odd = 0
even = 0
ans = 0

for i in num:
    if (i % 2 == 0):
        even +=1
    else:
        odd +=1

# 남은 숫자가 짝수냐 홀수냐?
if(even>odd and odd != 0):
    idx = 0
elif(even<odd and even != 0):
    idx = 1
elif(even>odd and odd == 0):
    idx = -1
elif(even<odd and even == 0):
    idx = -2



max_num = max(odd , even)
min_num = min(odd , even)
minus = abs(max_num - min_num)

ans += (max_num - minus) * 2


#짝수가 더 많고, 이전 홀수가 있을 때
if(idx == 0):
    if (minus != 0):
        ans += 1

#홀수가 더 많고, 이전 짝수가 있을 때
elif(idx == 1):
    if (minus % 3 == 0):
        ans += ((2 * minus) // 3)
    elif (minus % 3 == 1):
        ans += ( ((2 * minus) // 3) - 1)
    elif (minus % 3 == 2): 
        ans += ((2 * minus - 1) // 3)

#짝수로만 구성되어 있을 때
elif(idx == -1):
    ans = 1

#홀수로만 구성되어 있을 때  
elif(idx == -2):
    if (minus % 3 == 0):
        ans += ((2 * minus) // 3)
    elif (minus % 3 == 1):
        ans += ( ((2 * minus) // 3) - 1)
    elif (minus % 3 == 2): 
        ans += ((2 * minus - 1) // 3)


print(ans)



'''   
홀 홀홀(짝) 홀 홀홀(짝) 홀



홀
짝
홀 + 홀 = 짝
@홀 + 짝 = 홀
짝 + 짝 = 짝
'''