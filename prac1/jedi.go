package main

import "fmt"

func main() {
	x := sum()
	fmt.Println("Total is", x)
}

// func (r reciever) identifier(parameters(s)) (return(s)) { ... }
func sum(x ...int) int {
	fmt.Println(x)
	fmt.Printf("%T\n", x)

	sum := 0
	
	for _, v := range x {
		sum += v
	}
	fmt.Println(sum)
	return sum
}