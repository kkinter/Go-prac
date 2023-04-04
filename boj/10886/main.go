package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)
	voteMap := map[int]int{
		1: 0,
		0: 0,
	}

	for i := 0; i < n; i++ {
		var vote int
		fmt.Scanln(&vote)
		voteMap[vote] += 1
	}
	var maxVal int
	var maxKey int

	for k, v := range voteMap {
		if v > maxVal {
			maxVal = v
			maxKey = k
		}
	}

	if maxKey == 1 {
		fmt.Println("Junhee is cute!")
	} else if maxKey == 0 {
		fmt.Println("Junhee is not cute!")
	}
}
