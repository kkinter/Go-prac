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
	tree map[string][2]string
)

func preorder(root string, traverse []string) []string {
	if root != "." {
		traverse = append(traverse, root)
		traverse = preorder(tree[root][0], traverse)
		traverse = preorder(tree[root][1], traverse)
	}
	return traverse
}

func inorder(root string, traverse []string) []string {
	if root != "." {
		traverse = inorder(tree[root][0], traverse)
		traverse = append(traverse, root)
		traverse = inorder(tree[root][1], traverse)
	}
	return traverse
}

func postorder(root string, traverse []string) []string {
	if root != "." {
		traverse = postorder(tree[root][0], traverse)
		traverse = postorder(tree[root][1], traverse)
		traverse = append(traverse, root)
	}
	return traverse
}

func main() {
	f, err := os.Open("../input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner = bufio.NewScanner(f)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	tree = make(map[string][2]string)

	for i:=0; i < n; i++ {
		scanner.Scan()
		nodes := strings.Split(scanner.Text(), " ")
		tree[nodes[0]] = [2]string{nodes[1], nodes[2]}
	}

	fmt.Println(strings.Join(preorder("A", []string{}), ""))
	fmt.Println(strings.Join(inorder("A", []string{}), ""))
	fmt.Println(strings.Join(postorder("A", []string{}), ""))
}
