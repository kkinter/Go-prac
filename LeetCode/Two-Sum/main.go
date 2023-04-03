package main

import "fmt"

func main() {
	nums := []int{3, 2, 4}
	target := 6
	indexMap := make(map[int]int)
	for currIdx, currNum := range nums {
		requiredIdx, isPresent := indexMap[target-currNum]
		if isPresent {
			fmt.Println(requiredIdx, currIdx)
		}
		indexMap[currNum] = currIdx
	}
}