n = int(input())
string = input()

maxi = 0

for i in range(1,len(string)):
    for j in range(0,len(string)-i+1):
        tmp = string[j:j+i]
        for k in range(0,len(string)-i+1):
            if j == k:
                continue
            if tmp == string[k:k+i]:
                maxi = i
                break
print(maxi+1)