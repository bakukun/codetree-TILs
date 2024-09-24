n = int(input())
answer = []


def is_beautiful(answer):
    count = 1
    prev_digit = answer[0]

    for i in range(1,len(answer)):
        if answer[i] == prev_digit:
            count += 1

        else:
            if (count != prev_digit):
                return False
            count = 1
            prev_digit = answer[i]

    if(count % prev_digit == 0 or count == prev_digit):
        return True
    else:
        return False


def choose(curr_num):
    if curr_num == n + 1:
        if(is_beautiful(answer)):
            return 1
        return 0
    
    cnt = 0

    for i in range(1,5):
        answer.append(i)
        cnt += choose(curr_num + 1)
        answer.pop()

    return cnt

print(choose(1))