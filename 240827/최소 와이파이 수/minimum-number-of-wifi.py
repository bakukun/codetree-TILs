n, m = map(int, input().split())
people = list(map(int, input().split()))

i = 0
cnt = 0

while i < n:
    if people[i] == 1:
        cnt+=1
        i += (2*m)+1
    else:
        i += 1

print(cnt)