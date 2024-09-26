def permutation(num):
    if num == n:
        print_permutation()
        return

    for i in range(1,n+1):
        if (visited[i]):
            continue

        visited[i] = True
        arr.append(i)
        permutation(num+1)
        arr.pop()
        visited[i] = False
    return


def print_permutation():
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()


n = int(input())
arr = []
visited = [False] * (n+1)
permutation(0)