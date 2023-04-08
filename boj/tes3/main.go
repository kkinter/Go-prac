package main

import (
	"fmt"
	"sort"
)

func main() {
	emergency := []int{3, 76, 24}
	sortArr := make([]int, len(emergency))
	copy(sortArr[:], emergency[:])
  sort.Ints(sortArr)
	fmt.Println(emergency)
	fmt.Println(sortArr)
}