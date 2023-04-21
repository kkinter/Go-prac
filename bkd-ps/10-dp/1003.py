# https://bio-info.tistory.com/122

t = int(input())
for i in range(t):
    zero = [1, 0, 1]
    one = [0, 1, 1] 
    n = int(input())
    if n >= 3:
        for j in range(3, n + 1):
            zero.append(zero[j - 1] + zero[j - 2])
            one.append(one[j - 1] + one[j - 2])

 
    print(zero[n], one[n])