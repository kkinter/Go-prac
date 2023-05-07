import sys
sys.stdin = open("input.txt")

dy = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dx = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

dy4 = (-1, -1,  1, 1)
dx4 = (-1,  1, -1, 1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]


clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for d, s in moves:
    moved_clouds = []
    for y, x in clouds:
        ny = (y + dy[d] * s) % n
        nx = (x + dx[d] * s) % n
        board[ny][nx] += 1
        moved_clouds.append((ny, nx))

    for y, x in moved_clouds:
        cnt = 0
        for d in range(4):
            ny = y + dy4[d]
            nx = x + dx4[d]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            elif board[ny][nx] > 0:
                cnt += 1
        board[y][x] += cnt

    new_clouds = []
    for y in range(n):
        for x in range(n):
            if (y, x) in moved_clouds or board[y][x] < 2:
                continue
            board[y][x] -= 2
            new_clouds.append((y, x))
    clouds = new_clouds

res = 0
for y in range(n):
    for x in range(n):
        res += board[y][x]
print(res)
