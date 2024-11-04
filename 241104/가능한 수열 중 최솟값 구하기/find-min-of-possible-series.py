def is_okay(ans):
    length = len(ans) // 2
    tmp = 1
    for tmp in range(1, length + 1):
        for i in range(len(ans) - tmp):
            if (i + tmp * 2 > len(ans)):
                continue
            if ans[i:i + tmp] == ans[i + tmp:i + tmp * 2]:
                return False
    return True


def backtrack(n):
    global ans, minimum
    #print(ans)
    if (n == N):
        if (is_okay(ans)):
            minimum = min(minimum, int("".join(ans)))
            #print(minimum)
        return

    for i in num_list:
        ans.append(i)
        backtrack(n + 1)
        ans.pop()


N = int(input())
num_list = ['4', '5', '6']
ans = []
minimum = int('9' * N)

backtrack(0)
print(minimum)