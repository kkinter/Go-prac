package main

import "fmt"

func main() {
	var t int
	fmt.Scanln(&t)

	for i := 0; i < t; i++{
		var score int
		var input string
		var cnt int = 1
		fmt.Scanln(&input)

		for j := 0; j < len(input) - 1; j++{
			fmt.Println(j, len(input))
			if string(input[j]) == "O"{
				score += cnt
				if input[j] == input[j + 1]{
					cnt += 1
					if j + 1 == len(input) - 1{
						fmt.Println("Last", score, cnt)
						score += cnt
					}
				}
			} else if string(input[j]) == "X"{
				cnt = 1
			}
		}
		fmt.Println(score)
	}
}