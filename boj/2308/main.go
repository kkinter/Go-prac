package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func removeIndex(x []int, i int) []int{
	x = append(x[:i], x[i+1:]... )
	return x
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	n := 9
	var sum, prev, next int
	arr := make([]int, 9)

	for i := 0; i < n; i++{
		var height int 
		fmt.Fscanln(reader, &height)
		arr[i] = height
		sum += height
	}

	target := sum - 100
	sort.Ints(arr)

	for i := 0; i < n - 1; i++{
		for j := i + 1; j < n; j++{
			if arr[i] + arr[j] == target{
				prev = i
				next = j - 1
				break
			}
		}
	}
	arr = removeIndex(arr, prev)
	arr = removeIndex(arr, next)
	for _, v := range arr{
		fmt.Println(v)
	}
}