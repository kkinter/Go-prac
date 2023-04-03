nums = []
target = 0
seen = {}

for i, v in enumerate(nums):
    print(f"{i}번째 인덱스 {v} 일 때")

    # v 일 때 필요한 값
    remaining = target - nums[i]
    
    # v 일 때 필요한 값이 있으면,
    if remaining in seen:
        print(i, seen[remaining])
    
    # v 일 때 필요한 값이 없으면 seen 딕셔너리에 저장
    seen[v] = i 