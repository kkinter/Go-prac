package main

import "fmt"

func main() {
	nums := []int{3, 3}
	var res []int
	target := 6

	for i, vi := range nums {
		for j, vj := range nums[i+1:] {
			if vi + vj == target {
				fmt.Println(vi, vj)
				res = append(res, i)
				res = append(res, j + i + 1)
			}
		}
	}
	fmt.Println(res)
}
