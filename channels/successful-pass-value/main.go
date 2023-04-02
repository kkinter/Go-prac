package main

// 프로그램의 진입점인 main
import "fmt"

func main() {
	
	c := make(chan int)

	go func ()  {
		c <- 42
	}()

	fmt.Println(<-c)
}