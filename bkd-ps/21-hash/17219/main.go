package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	f, err := os.Open("../input.txt")

	if err != nil{
		panic(err)
	}
	defer f.Close()

	var reader *bufio.Reader = bufio.NewReader(f)
	//var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int

	fmt.Fscanln(reader, &n, &m)
	passwordMap := make(map[string]string)
	for i := 0; i < n; i++{
		var site, password string
		fmt.Fscanln(reader, &site, &password)
		passwordMap[site] = password
	}

	for i := 0; i < m; i++{
		var site string
		fmt.Fscanln(reader, &site)
		fmt.Fprintln(writer, passwordMap[site])
	}
}