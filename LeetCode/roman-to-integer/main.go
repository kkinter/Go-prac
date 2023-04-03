package main

import "fmt"

func main() {
	s := "III"
	for i := 0; i < len(s); i++ {
		fmt.Printf("%c\n",s[i])
		a, _ := fmt.Scanf("%c", s[i])
		fmt.Println(a)
	}
}