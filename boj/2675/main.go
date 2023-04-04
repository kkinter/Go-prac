package main

import "fmt"

func main() {
	var t int
	fmt.Scanln(&t)

	for i := 0; i < t; i++{
		var r int
		var s string
		fmt.Scanln(&r, &s)
		for k := 0; k < len(s); k++{
			for j := 0; j < r; j++{
				fmt.Printf("%c", s[k])
			}
		}
		fmt.Println()
	}
}