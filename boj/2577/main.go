package main

import (
	"fmt"
	"strconv"
)

func main() {
	var a, b, c int
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Scanln(&c)

	val := strconv.Itoa(a * b * c)
	arr := make([]int, 10)

	for i := 0; i < len(val); i++{
		arr[val[i] - '0']++
	}

	for _, v := range arr{
		fmt.Println(v)
	}
}
/*
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var a, b, c int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanf(reader, "%d\n%d\n%d\n", &a, &b, &c)
	var result = a * b * c
	var counts = make([]int, 10)
	for true {
		counts[result%10]++
		result /= 10
		if result == 0 {
			break
		}
	}

	for i := range counts {
		fmt.Println(counts[i])
	}
}
*/