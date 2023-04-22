import sys
sys.stdin = open("input.txt")
input = sys.stdin.read

n, *s = input().split()
for i in range(len(s)):
    s[i] = s[i][::-1]
s = list(map(int, s))

print(*sorted(s), sep = '\n')
"""
readline() 은 줄바꿈 문자를 볼 때 까지 읽어들이는 함수입니다.
read(bytes_to_read) 는 지정된 byte 만큼 읽어들입니다.
bytes_to_read 를 지정하지 않고 read() 를 호출하면 입력이 끝날 때 까지 모든 내용을 읽어들입니다.
"계속 입력을 받고 안 끝나는" 이유는 프로그램에게 입력이 끝났다 라는 사실을 알려주지 못했기 때문입니다.
사용하고 계신 컴퓨터에 따라 Ctrl+Z 또는 Ctrl+D 를 누르면 입력을 끝낼 수 있습니다.
"""