n,m = map(int,input().split())
people = list(map(int,input().split()))

ans = n // (2*m +1)
if(ans == 0):
    print(1)
else:
    print(ans)