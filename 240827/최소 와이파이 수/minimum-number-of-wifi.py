n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0  # 와이파이 설치 횟수

def find_next_index(current_index):
    """현재 위치 이후로 가장 가까운 1의 위치를 찾습니다."""
    for idx in range(current_index, n):
        if arr[idx] == 1:
            return idx
    return current_index  # 더 이상 1이 없으면 현재 위치 반환

while True:
    # 현재 위치에서 와이파이 설치 가능 여부 확인
    i = find_next_index(i if 'i' in locals() else 0)
    if arr[i:i + 2 * m + 1].count(1) == 0:
        break  # 더 이상 설치할 필요가 없으면 종료
    
    cnt += 1  # 와이파이 설치
    i += 2 * m + 1  # 설치된 와이파이 범위를 넘어서 탐색 위치 이동

print(cnt)