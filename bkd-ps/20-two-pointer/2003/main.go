package main

import (
	"bufio"
	"fmt"
	"os"
)

func sum(nums []int) (total int) {
	num := 0
	for i := 0; i < len(nums); i++{
		num = nums[i]
		total += num
	}
	return total
}

func main() {
	// f, err := os.Open("../input.txt")
	// if err != nil {
	// 	panic(err)
	// }
	// defer f.Close()

	//var reader *bufio.Reader = bufio.NewReader(f)
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	var nums []int

	fmt.Fscanln(reader, &n, &m)
	nums = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d", &nums[i])
	}

	var l, r, cnt int
	l, r, cnt = 0, 1, 0

	for r <= n && l <= r{
		tmp := sum(nums[l:r])
		if tmp == m{
			cnt++
			r++
		} else if tmp < m{
			r++
		} else{
			l++
		}
	}
	fmt.Fprintln(writer, cnt)
}