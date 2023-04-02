package main

import "fmt"

// fatal error: all goroutines are asleep - deadlock!
// 채널이 막혔기 때문
func main() {
	// 정수를 넣는 채널
	// <- 뭔가를 넣으라는 표시
	// 채널의 개념은 데이터를 보낼 수 있는 공간
	c := make(chan int)

	// 여기에 와선 채널에 42를 넣고 차단함
	// 이 프로그램이 실행되면서 main에 진입하고 채널을 생성했는데 
	// 채널에서 수신하는 작업이 없습니다
	// 트랜잭션이 발생하려면 송수신이 동시에 실행될 수 있어야 함
	c <- 42

	fmt.Println(<-c)
}