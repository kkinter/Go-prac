package main

import "fmt"

func main() {
	n, err := fmt.Println("Hello World", 23, true)
	x, _ := fmt.Println("Hello World", 23, true)
	fmt.Println(n, err)
	fmt.Println(x)
	foo()
	fmt.Println("something more", 42, true)
	for i := 0; i < 10; i++ {
		if i%2 == 0 {
			fmt.Println(i)
		}
	}
	bar()
}

func foo() {
	fmt.Println("I'm in foo")
}

func bar() {
	fmt.Println("and then we exited")
}
