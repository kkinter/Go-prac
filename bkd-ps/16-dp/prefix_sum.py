def prefix_sum(arr):
    n = len(arr)  # 배열의 길이
    prefix = [0] * (n + 1)  # prefix 배열 초기화

    for i in range(1, n + 1):  # 1부터 n까지 반복
        prefix[i] = prefix[i - 1] + arr[i - 1]  # prefix[i] = prefix[i-1] + arr[i-1], 현재 원소까지의 누적 합 저장

    return prefix

def interval_sum(prefix, left, right):
    return prefix[right] - prefix[left - 1]  # right까지의 누적 합에서 left-1까지의 누적 합을 빼면 left부터 right까지의 구간 합이 됨

# 사용 예시
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 입력 배열
prefix = prefix_sum(arr)  # 입력 배열의 누적 합(prefix sum) 계산
left = 2  # 구간의 시작 인덱스
right = 5  # 구간의 끝 인덱스
result = interval_sum(prefix, left, right)  # 구간 합 계산
print("구간 합:", result)