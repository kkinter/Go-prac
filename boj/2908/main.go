package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscanf(reader, "%d %d\n", &a, &b)
	fmt.Println(a, b)

	strNumA := strconv.Itoa(a)
	strNumB := strconv.Itoa(b)

	strArrA := []string{
		strNumA[0], strNumA[1], strNumA[2], 
	}
	strArrB := []string{strNumB}

	fmt.Println(strArrA, strArrB)
	for i, v := range strArrA{
		fmt.Println(i, v)
	}
  
}