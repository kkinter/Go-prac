package main

import "fmt"


func main() {
	var s int
	fmt.Scan(&s)

	n := 1
	for n*(n+1)/2 <= s {
		n++
	}

	fmt.Println(n - 1)
}