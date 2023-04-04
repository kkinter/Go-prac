package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	reversed := strings.Builder{}
	for i := len(s) - 1; i >= 0; i--{
		reversed.WriteByte(s[i])
	}

	if s == reversed.String(){
		fmt.Println(1)
	}else{
		fmt.Println(0)
	}
}