from collections import deque
n, m = map(int, input().split())
MAX = 100001
arr = [0] * MAX

def bfs():
    que = deque()
    que.append(n)
    while que:
        cur = que.popleft()
        if cur == m:
            return arr[cur]
        
        dx = (cur -1, cur + 1, cur * 2)
        for d in dx:
            if 0 <= d < MAX and not arr[d]:
                arr[d] = arr[cur] + 1
                que.append(d)

print(bfs())

