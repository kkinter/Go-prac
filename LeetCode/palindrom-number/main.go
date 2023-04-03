package main

import "fmt"

// https://www.code-recipe.com/post/palindrome-number
func main() {
	x := 121234
	var reversedNum int
	tmp := x
	// tmp 121 일 때, reversedNum 은 0
	// 1. tmp 12, reversedNum =
	for tmp > 0 {
		fmt.Println("Before temp", tmp)
		fmt.Println("Before revN", reversedNum)
		reversedNum = reversedNum*10 + tmp%10
		tmp = tmp / 10
		fmt.Println("after  temp", tmp)
		fmt.Println("after  revN", reversedNum)
	}
}