package main

import "fmt"

var y = 42
var z string= "lorem ipsum"
var a string = `"james said,"`

func main() {
	fmt.Println(y)
	fmt.Printf("%T\n", y)
	y = 43
	fmt.Println(y)
	fmt.Println(z)
	fmt.Printf("%T\n", z)
	fmt.Println(a)
}