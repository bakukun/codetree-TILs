n,m = map(int,input().split())
people = list(map(int,input().split()))

i = 0
cnt = 0


while i < n:
    if (people[i] == 1):
        wifi = i
        for k in range(i+1,min(i+m+1,n)):
            if(people[k] == 1):
                wifi = k
        cnt +=1
        i = wifi + m + 1
    else:
        i += 1
print(cnt)