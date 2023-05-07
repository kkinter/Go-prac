package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	graph map[int][]int
	parent []int
	visited []bool
	scanner *bufio.Scanner
	writer  *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	f, err := os.Open("../input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	

	scanner = bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	n := scanInt()
	graph = make(map[int][]int, n+1)
	parent = make([]int, n+1)
	visited = make([]bool, n+1)

	for i := 1; i <= n-1; i++ {
		a, b := scanInt(), scanInt()
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}

	dfs(1)

	for i := 2; i <= n; i++ {
		writer.WriteString(strconv.Itoa(parent[i]) + "\n")
	}
}

func dfs(node int) {
	visited[node] = true
	for _, adjacentNode := range graph[node] {
		if !visited[adjacentNode] {
			parent[adjacentNode] = node
			dfs(adjacentNode)
		}
	}
}

func scanInt() int {
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	return n
}