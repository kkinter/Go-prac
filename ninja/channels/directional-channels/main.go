package main

import "fmt"


func main() {
	c := make(chan int)
	cr := make(<- chan int) // 수신
	cs := make(chan <- int) // 송신

	fmt.Println("_______")
	fmt.Printf("c\t%T\n", c)
	fmt.Printf("cr\t%T\n", cr)
	fmt.Printf("cs\t%T\n", cs)

}