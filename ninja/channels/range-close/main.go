package main

import "fmt"

func main() {
	c := make(chan int)
	// send
	go func() {
		for i := 0; i < 100; i++ {
			c <- i
		}
		// 채널 닫기
		// 주 채널이 닫힘
		close(c)
	}()

	// receive
	for v := range c {
		fmt.Println(v)
	}

	fmt.Println("about to exit")
}
