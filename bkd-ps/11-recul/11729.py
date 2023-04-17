# https://kbwplace.tistory.com/115
def hanoi(num, from_, to, other):
    if num == 0: return # base case
    hanoi(num-1, from_, other, to)
    print(from_, to)
    hanoi(num-1, other, from_, to)

# hanoi(n, 1, 3, 2)

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)

    hanoi_tower(n-1, start, 6-start,end) # 1단게
    print(start, end)                    # 2단계
    hanoi_tower(n-1, 6-start-end, end)   # 3단계

def TowerOfHanoi(n , s_pole, d_pole, i_pole):           
    if n == 1:
        print("Move disc 1 from pole",s_pole,"to pole",d_pole)
        return
    TowerOfHanoi(n-1, s_pole, i_pole, d_pole)
    print("Move disc",n,"from pole",s_pole,"to pole",d_pole)
    TowerOfHanoi(n-1, i_pole, d_pole, s_pole)
 
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of poles