package main

import "fmt"

var y = 43

// DECLARE there is a variable z
var z int

func main() {
	// short declartion operator
	// Declare a variable and assign a value (of a certain TYPE)
	x := 42
	fmt.Println(x)
	
	fmt.Println(y)
	foo()
	fmt.Println(z)
}

func foo() {
	fmt.Println("again:", y)
}
