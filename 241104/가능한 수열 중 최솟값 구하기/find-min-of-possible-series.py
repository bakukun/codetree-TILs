def is_okay(ans):
    length = len(ans)
    for l in range(1, length // 2 + 1):
        if ans[-l:] == ans[-2*l:-l]:
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
        if is_okay(ans):
            backtrack(n + 1)
        ans.pop()


N = int(input())
num_list = ['4', '5', '6']
ans = []
minimum = int('9' * N)

backtrack(0)
print(minimum)