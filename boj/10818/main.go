package main

import (
	"fmt"
)

func main() {
	var t int
	fmt.Scan(&t)

	nums := make([]int, t)
	for i := 0; i < t; i++{
		fmt.Scan(&nums[i])
	}

	var maxVal int = 0
	var minVal int = 1_000_000

	for _, v :=  range nums{
		if maxVal < v{
			maxVal = v
		}
		if minVal > v{
			minVal = v
		}
	}
	fmt.Println(maxVal, minVal)
}