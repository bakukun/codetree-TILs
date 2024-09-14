n = int(input())
memo = [-1] * (n+1)

def fibo(x):
    if memo[x] != -1:
        return memo[x] 
    if x == 1:               
        memo[x] = 1   
    elif x == 2:               
        memo[x] = 2   
    else:
        memo[x] = (fibo(x-1) + fibo(x-2)) % 10007
    return memo[x]


fibo(n)

print(memo[n])