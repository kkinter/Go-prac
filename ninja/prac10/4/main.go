package main

import (
	"fmt"
)

func main() {
	// quit 를 의미
	q := make(chan int)
	c := gen(q)

	receive(c, q)

	fmt.Println("about to exit")
}
func receive(c <-chan int, q <-chan int){
	for {
		select{
		case v := <-c:
		fmt.Println(v)
		case <-q:
		return
		}
	}
}
// 인자 q 는 수신/읽기 전용 채널 
func gen(q chan<- int) <-chan int {
	// 읽기 전용 채널
	c := make(chan int)

	go func ()  {
		for i := 0; i < 100; i++ {
		c <- i
		}
		// q 에 값이 들어가면 빼야함
		// 채널에 1을 넣는 것
		q <- 1
		close(c)
	}()
	

	return c
}