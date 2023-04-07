package main

import "fmt"

func main() {
	str := "hello 세계"
	for _, v := range str {
		fmt.Printf("%T, %c\n", v, v) // int32
	}
}