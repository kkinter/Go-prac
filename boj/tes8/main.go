package main

import "fmt"

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func solution(a int, b int) int {
	x := gcd(a, b)
	d := b / x
	if d == 1 {
		return 1
	}
	div := 2
	for d > 1 {
		for d % div == 0 {
			fmt.Println("들어옴")
			if !(div == 5 || div == 2) {
				return 2
			}
			d /= div
		}
		div++
	}

	return 1
}
func main() {
	fmt.Println(solution(7, 20))
}