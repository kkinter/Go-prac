package main

import "fmt"

func main() {
	c := make(chan int)
	// send
	go foo(c)

	// receive
	bar(c)

	fmt.Println("about to exit")
}

// send
// 참조 타입?
func foo(c chan<- int) {
	c <- 42
}

// receive
func bar(c <- chan int) {
	// 값을 빼고 출력
	fmt.Println(<-c)
}