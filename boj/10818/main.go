package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var t int
	reader := bufio.NewReader(os.Stdin)
  fmt.Fscan(reader, &t)

	nums := make([]int, t)
	for i := 0; i < t; i++{
		fmt.Fscan(reader, &nums[i])
	}

	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	fmt.Printf("%d %d\n", nums[0], nums[t - 1])
}