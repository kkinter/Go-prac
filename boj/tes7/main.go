package main

import (
	"fmt"
	"strconv"
)

func main() {
	s := "12343465"
	num, _ := strconv.ParseInt(s, 10, 64)
	fmt.Println(num)
}