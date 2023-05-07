package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Cctv struct {
	cctvType int
	i, j     int
}

var (
	scanner    *bufio.Scanner
	dx         = []int{0, 1, 0, -1}
	dy         = []int{1, 0, -1, 0}
	directions = [][][]int{
		{{}},
		{{0}, {1}, {2}, {3}},
		{{0, 2}, {1, 3}},
		{{0, 1}, {1, 2}, {2, 3}, {0, 3}},
		{{0, 1, 2}, {0, 1, 3}, {1, 2, 3}, {0, 2, 3}},
		{{0, 1, 2, 3}},
	}
	minValue int = math.MaxInt32
)

func fill(matrix [][]int, directions []int, x, y int) {
	for _, direction := range directions {
		nx := x
		ny := y
		for {
			nx += dx[direction]
			ny += dy[direction]

			if nx < 0 || ny < 0 || nx >= len(matrix) || ny >= len(matrix[0]) {
				break
			}

			if matrix[nx][ny] == 6 {
				break
			} else if matrix[nx][ny] == 0 {
				matrix[nx][ny] = -1
			}
		}
	}
}

func dfs(depth int, matrix [][]int, cctvs []Cctv) {
	if depth == len(cctvs) {
		count := 0
		for i := 0; i < len(matrix); i++ {
			for j := 0; j < len(matrix[0]); j++ {
				if matrix[i][j] == 0 {
					count++
				}
			}
		}
		minValue = min(minValue, count)
		return
	}

	cctvNum, x, y := cctvs[depth].cctvType, cctvs[depth].i, cctvs[depth].j

	for _, direction := range directions[cctvNum] {
		tmp := copyMatrix(matrix)
		fill(tmp, direction, x, y)
		dfs(depth+1, tmp, cctvs)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func copyMatrix(matrix [][]int) [][]int {
	copyM := make([][]int, len(matrix))
	for i := range matrix {
		copyM[i] = make([]int, len(matrix[i]))
		copy(copyM[i], matrix[i])
	}
	return copyM
}

func main() {
	f, err := os.Open("../input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner = bufio.NewScanner(f)
	scanner.Scan()
	input := strings.Split(scanner.Text(), " ")

	n, _ := strconv.Atoi(input[0])
	m, _ := strconv.Atoi(input[1])

	matrix := make([][]int, n)
	cctvs := []Cctv{}

	for i := 0; i < n; i++ {
		scanner.Scan()
		row := strings.Split(scanner.Text(), " ")
		matrix[i] = make([]int, m)

		for j := 0; j < m; j++ {
			val, _ := strconv.Atoi(row[j])
			matrix[i][j] = val
			if val >= 1 && val <= 5 {
				cctvs = append(cctvs, Cctv{cctvType: val, i: i, j: j})
			}
		}
	}

	dfs(0, matrix, cctvs)
	fmt.Println(minValue)
}
