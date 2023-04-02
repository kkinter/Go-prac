package main

import "fmt"


func main() {
	// 버퍼 채널로 만들기
	// 버퍼 채널은 값을 수신할 주체가 없어도 
	// 채널 안에 값이 머물 수 있게 해줌

	c := make(chan int, 2) // 값 하나가 머물러 있게 함

	c <- 42
	c <- 43

	fmt.Println(<-c)
	fmt.Println(<-c)
}