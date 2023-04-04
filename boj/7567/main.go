package main

import "fmt"

type Stack []string

func (s *Stack) Push(val string) {
	*s = append(*s, val)
}

func (s *Stack) Pop() (string, bool) {
	idx := len(*s) - 1
	if idx < 0 {
		return "", false
	}
	val := (*s)[idx]
	*s = (*s)[:idx]
	return val, true
}

func main() {
	// var s Stack
	var input string
	sum := 10

	fmt.Scanln(&input)
	for i := 0; i < len(input) - 1; i++ {
		if input[i] == input[i + 1]{
			sum += 5
		} else {
			sum += 10
		}
		//s.Push(string(input[i]))
	}
	fmt.Println(sum)
	//fmt.Println(s)
}
