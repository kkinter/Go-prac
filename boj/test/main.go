package main

import (
	"fmt"

	"strings"
)

func main() {
	str := "hello 세계"
	// tmp := strings.ToLower(str)
	z := strings.Split(str, " ")
	// sort.Slice(tmp, func(i, j int) bool {
	// 	return tmp[i] < tmp[j]
	// })
	fmt.Println(z)
}