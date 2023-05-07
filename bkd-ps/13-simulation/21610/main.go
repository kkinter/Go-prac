package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)



var (
	scanner *bufio.Scanner
	dy8 = []int{10, 0, -1, -1, -1, 0, 1, 1, 1}
	dx8 = []int{-1, -1, -1, 0, 1, 1, 1, 0, -1}
	dy4 = []int{-1, -1, 1, 1}
	dx4 = []int{-1, 1, -1, 1}
)

func main() {
	f, err := os.Open("../input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner = bufio.NewScanner(f)
	scanner.Scan()

	values := strings.Split(scanner.Text(), " ")
	n, _ := strconv.Atoi(values[0])
	m, _ := strconv.Atoi(values[1])

	board := make([][]int, n)
	for i:=0; i < n; i++{
		scanner.Scan()
		row := strSilceToIntSlice(strings.Split(scanner.Text(), " "))
		board[i] = append(board[i], row...)
	}

	moves := make([][]int, m)
	for i := range moves{
		scanner.Scan()
		values := strings.Split(scanner.Text(), " ")
		x, _ := strconv.Atoi(values[0])
		y, _ := strconv.Atoi(values[1])
		moves[i] = []int{x, y}
	}

	clouds := [][]int{
		{n-1, 0},
		{n-1, 1},
		{n-2, 0},
		{n-2, 1},
	}

	for _, move := range moves{
		d, s := move[0], move[1]
		moved_clouds := [][]int{}
		for _, cloud := range clouds{
			y, x := cloud[0], cloud[1]
			ny := mod(y, dy8[d], s, n)
			nx := mod(x, dx8[d], s, n)
			board[ny][nx] += 1

			moved_clouds = append(moved_clouds, []int{nx, ny})
		}
		for _, cloud := range moved_clouds{
			y, x := cloud[0], cloud[1]
			cnt := 0
			for i := 0; i < 4; i++{
				ny := y + dy4[i]
				nx := x + dx4[i]
				if ny < 0 || nx < 0 || ny >= n || nx >= 0{
					continue
				} else if board[ny][nx] > 0{
						cnt++
				}
			}
			board[y][x] += cnt
		}

		new_clouds := [][]int{}
		
		for i:=0; i < n; i++{
			for j:=0; j < n; j++{
				found := false
				for _, cloud := range moved_clouds {
					if cloud[0] == i && cloud[1] == j {
						found = true
						break
					}
				}
				if found || board[i][j] < 2{
					continue
				}
				board[i][j] -= 2
				new_clouds = append(new_clouds, []int{i, j})
			}
		}
		clouds = new_clouds
	}

	res := 0
	for y:=0; y < n; y++{
		for x:=0; x < n; x++{
			res += board[y][x]
		}
	}
	fmt.Println(res)
}

func mod(x, delta, s, n int) int {
	nx := (x + delta * s) % n
	if nx < 0 {
		nx += n
	}
	return nx
}

func strSilceToIntSlice(s []string) []int {
	var n []int
	for _, val := range s{
		w, _ := strconv.Atoi(val)
		n = append(n, w)
	}
	return n
}