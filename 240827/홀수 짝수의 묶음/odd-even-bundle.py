n = int(input())
num = list(map(int, input().split()))
odd = 0
even = 0
ans = 0


for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1


def calculate_groups(even, odd):
    group_num = 0

    while even > 0 or odd > 0:
        if group_num % 2 == 0:
            # 짝수 그룹을 만들 때
            if even > 0:
                even -= 1
            elif odd >= 2:
                odd -= 2
            else:
                group_num -= 1
                break
        else:
            # 홀수 그룹을 만들 때
            if odd > 0:
                odd -= 1
            else:
                break
        group_num += 1
    
    return group_num

ans = calculate_groups(even, odd)
print(ans)