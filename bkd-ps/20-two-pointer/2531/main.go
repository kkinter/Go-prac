package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func max(a float64, b float64) float64{
	if a > b{
		return a
	} else {
		return b
	}
}

func main() {
	f, err := os.Open("../input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	//var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var reader *bufio.Reader = bufio.NewReader(f)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, d, k, c int
	var sushi []int

	fmt.Fscanln(reader, &n, &d, &k, &c)

	sushi = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d\n", &sushi[i])
	}
	
	var l, r = 0, k-1
	sushiMap := make(map[int]int)

	sushiMap[c] += 1
	for i := 0; i < r+1; i++{
		sushiMap[sushi[i]] += 1 
	}
	res := math.Inf(-1)
	for l < n{
		res = max(res, float64(len(sushiMap)))

		sushiMap[sushi[l]] -= 1
		if sushiMap[sushi[l]] == 0{
			delete(sushiMap, sushi[l])
		}
		l++
		r++
		sushiMap[sushi[r % n]] += 1
	}
	fmt.Println(int(res))
}