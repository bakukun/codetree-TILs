n, m = map(int, input().split())
people = list(map(int, input().split()))

i = 0
cnt = 0

while i < n:
    if people[i] == 1:
        # 사람이 있는 곳부터 오른쪽으로 이동하면서 가장 멀리 있는 사람을 찾음
        install_pos = i  # 와이파이를 설치할 위치
        for k in range(i + 1, min(i + m + 1, n)):
            if people[k] == 1:
                install_pos = k
        # 찾은 위치에 와이파이 설치
        cnt += 1
        i = install_pos + (2 * m) + 1  # 와이파이 커버 범위 이후로 이동
    else:
        i += 1

print(cnt)