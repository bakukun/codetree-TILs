def is_okay(ans):
    length = len(ans) // 2
    for tmp in range(1, length + 1):
        for i in range(len(ans) - tmp):
            if ans[i:i + tmp] == ans[i + tmp:i + tmp * 2]:
                return False
    return True

def backtrack(n):
    global ans, found
    
    if found:
        return  

    if n == N:
        print("".join(ans))
        found = True  
        return

    for i in num_list:
        ans.append(i)
        if is_okay(ans):
            backtrack(n + 1)
            if found:
                return 
        ans.pop()

N = int(input())
num_list = ['4', '5', '6']
ans = []
found = False

backtrack(0)