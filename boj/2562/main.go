package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	nx := make([]int, 9)

	for i := 0; i < 9; i++{
		fmt.Fscanln(reader, &nx[i])
	}
	
	var maxVal int = 0
	var idx int 

	for i, v := range nx{
		if maxVal < v{
			maxVal = v
			idx = i
		}
	}
	fmt.Println(maxVal)
	fmt.Println(idx + 1)
}

// package main

// import (
// 	"fmt"
// 	"bufio"
// 	"os"
// )

// func main() {
// 	var numbers = make([]int, 9)
// 	reader := bufio.NewReader(os.Stdin)
// 	var max = 0
// 	var maxIndex = 0
// 	for i := range numbers {
// 		fmt.Fscanf(reader, "%d\n", &numbers[i])
// 		if numbers[i] > max {
// 			max = numbers[i]
// 			maxIndex = i
// 		}
// 	}

// 	fmt.Println(max)
// 	fmt.Println(maxIndex+1)
// }